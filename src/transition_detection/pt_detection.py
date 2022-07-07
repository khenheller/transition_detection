from scipy.signal import find_peaks
from ahrs.filters import Madgwick
import numpy as np
import pandas as pd
import pywt
from pyquaternion import Quaternion
from scipy.integrate import cumtrapz
from src.transition_detection.test_types import test_types
from src.transition_detection.is_empty import is_empty


def pt_detection(locs, fs, acc, gyro, pitch, sin_theta_pks):
    """Detects transitions from sitting to standing and the opposite.

    Args:
        locs (np.ndarray): Locations of peaks.
        fs (int): Sampling rate in Hz.
        acc (np.ndarray): accelerometer signals.
        gyro (np.ndarray): Gyroscope signals.
        pitch (np.ndarray): angle.
        sin_theta_pks (np.ndarray): Peaks in angle.

    Returns:
        sit_2_stand (np.ndarray): All transitions from sit to stand
        stand_2_sit (np.ndarray): All transitions from stand to sit
    """

    test_types(
        var_list=[locs, fs, acc, gyro, pitch, sin_theta_pks],
        var_name_list=["locs", "fs", "acc", "gyro", "pitch", "sin_theta_pks"],
        type_list=[np.ndarray, int, np.ndarray, np.ndarray, np.ndarray, np.ndarray],
    )
    is_empty(
        var_list=[locs, fs, acc, gyro, pitch, sin_theta_pks],
        var_name_list=["locs", "fs", "acc", "gyro", "pitch", "sin_theta_pks"],
    )

    fuse = Madgwick()
    sit_2_stand = []
    stand_2_sit = []

    # Iterate peaks.
    for peak, peak_idx in zip(sin_theta_pks, locs):

        # Mark epochs of 15sec before and after peaks.
        epoch = list(range(peak_idx - 15 * fs, peak_idx + 15 * fs))
        epoch_length = len(epoch)

        # Detection of onset/offset of PT according to pitch pattern.
        try:
            coeffs = pywt.wavedec(data=pitch[epoch], wavelet="coif5", level=10)
            dwt1 = pywt.upcoef(part="a", coeffs=coeffs[:, 0], wavelet="coif5", level=5)
            dwt2 = pywt.upcoef(part="a", coeffs=coeffs[:, 0], wavelet="coif5", level=9)

        except Exception as err:
            raise Exception(f"Epoch too big: {err}")

        else:
            pitch_denoised = (dwt1 - dwt2) * np.pi / 180
            pk_locs, _ = find_peaks(x=pitch_denoised, height=0.1, prominance=0.05)

            # If no peaks were detected, continue.
            if not (bool(pk_locs)):
                continue

            # Denoise data.
            pitch_denoised_series = pd.Series(pitch_denoised)
            pitch_denoised_series.rolling(window=30, win_type="gaussian", inplace=True)
            pitch_denoised = np.array(pitch_denoised_series)

            # Find start of peak and end of peak.
            pre_peak = (epoch_length / 2) - (2 * fs)
            post_peak = epoch_length / 2
            section = list(range(pre_peak, post_peak + 1))
            pk1 = np.argmin(pitch_denoised[section])
            pk1 = pk1 + pre_peak
            pre_peak = epoch_length / 2
            post_peak = (epoch_length / 2) + (3 * fs)
            section = list(range(pre_peak, post_peak + 1))
            pk2 = np.argmax(pitch_denoised[section])
            pk2 = pk2 + pre_peak
            # Recognize start and end of transition.
            diff_from_prev = np.diff(pitch_denoised[0:pk1])
            greater_than_prev = np.sign(diff_from_prev)
            extreme_points = np.diff(greater_than_prev)
            big_pitch = pitch_denoised[0: pk1 - 2] > -0.2
            big_extreme_points = np.logical_and(extreme_points, big_pitch)
            last_extreme_point = np.nonzero(big_extreme_points)[-1]

            t_start = last_extreme_point + 1

            diff_from_prev = np.diff(pitch_denoised[pk2 - 1:])
            greater_than_prev = np.sign(diff_from_prev)
            extreme_points = np.diff(greater_than_prev)
            small_pitch = pitch_denoised[pk2 - 1: -2] < -0.2
            big_extreme_points = np.logical_and(extreme_points, small_pitch)
            last_extreme_point = np.nonzero(big_extreme_points)[0]

            t_end = last_extreme_point - 1
            t_end = t_end + pk2

            # If no transition was found, skip.
            if np.logical_or(not (bool(t_start)), not (bool(t_end))):
                continue

            # Calculates the physical location in space and its HeEtek.
            # Fusion of accl & angular velocity  => to get orientation (Kalman filter method)
            q0 = Quaternion(0, 0.7, 0, 0.7)
            q = fuse.updateIMU(
                q0, gyr=gyro[epoch - 1, :] * (np.pi / 180), acc=acc[epoch - 1, :]
            )
            q = Quaternion(q)
            # q = compact(q)
            nq = q.normalized
            a = np.hstack(np.zeros(len(epoch), 1), acc[epoch - 1, :])
            nq = Quaternion(nq)
            a = Quaternion(a)
            ae = (nq * a) * nq.conjugate
            ae = ae[:, 1:4]
            at = ae - [np.zeros(len(ae), 2), np.ones(len(ae), 1)] * 9.81

            t0 = t_start
            t1 = t_end
            y_integ = at[t0:t1, 2]
            x_integ = np.arange(0, len(at[t0:t1])) / fs
            v_vertical = cumtrapz(y=y_integ, x=x_integ)
            kv = v_vertical[-1] / (t1 - t0)
            dv = kv * np.arange(0, (t1 - t0) + 1) - kv
            v_vertical = v_vertical - np.transpose(dv)

            y_integ = v_vertical
            x_integ = np.arange(0, len(np.arange(t0, t1 + 1))) / fs
            x_vertical = cumtrapz(y=section, x=x_integ)
            xt = x_vertical[-1] - x_vertical[t_start - t0]

            # HeEtek of end and start, check if HeEtek is negative or pos.
            if xt > 0:
                xt = np.max(x_vertical)
                pks_ind, properties = find_peaks(
                    x=v_vertical, height=0.2, prominance=0.15
                )
                pks = properties["peak_heights"]
                sorted_idx = np.flip(np.argsort(pks))
                pks_ind = pks_ind[sorted_idx]
                pks = pks[sorted_idx]
            else:
                xt = np.min(x_vertical)
                pks_ind, properties = find_peaks(
                    x=-v_vertical, height=0.2, prominance=0.15
                )
                pks = properties["peak_heights"]
                sorted_idx = np.flip(np.argsort(pks))
                pks_ind = pks_ind[sorted_idx]
                pks = pks[sorted_idx]

            if bool(pks):
                max_vt = pks[1]
            else:
                continue

            duration = (t_end - t_start) / fs

            # If HeEtek too long than is not transition.
            if (np.abs(xt) < 0.12) | (duration > 5) | (duration < 1.5):
                continue

            # Check if sit to stand or stand to sit.
            if xt > 0:
                sit_2_stand = np.vstack(
                    sit_2_stand, np.array([peak_idx, 1, duration, max_vt, xt, peak])
                )
            else:
                stand_2_sit = np.vstack(
                    stand_2_sit, np.array([peak_idx, 2, duration, max_vt, xt, peak])
                )

    return sit_2_stand, stand_2_sit
