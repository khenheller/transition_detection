import numpy as np
from scipy.integrate import cumtrapz
from scipy.signal import find_peaks
import pywt


def find_pt_with_theta(pitch: np.ndarray, fs: int):
    """Finds suspected postural transitions.

    Args:
        pitch (np.ndarray): Angle of sensor
        np (int): Sampling rate in Hz

    Raises:
        ValueError: pitch contained NaNs.

    Returns:
        locs (np.ndarray): peak indices
        sin_theta_pks (np.ndarray): peak heights
    """   
    if np.any(np.isnan(pitch)):
        raise ValueError("Pitch contains nans")

    samples_per_minute = 60 * fs
    # Divide pitch to 1 min sections.
    y = np.reshape(pitch, (samples_per_minute, pitch.size / samples_per_minute))

    # Theta Discrete wave transform.
    theta_dwt = []
    # Iterate over each minute.
    for section in y:
        # Calc pitch integral.
        tilt_angle = cumtrapz(y=section, x=list(range(0, section.size)) / fs)
        # Wavelet decomposition.
        level = 10  # Num of decomposition steps.
        wavelet_type = "coif5"
        coeffs = pywt.wavedec(data=tilt_angle, wavelet=wavelet_type, level=level)
        """Print coeffs, it looks like this:
        [cA_n, cD_n, cD_n-1, ..., cD2, cD1], cA is approximation coeffs, cD are details coefs.
        Next line uses only cA_n so make sure the dimention it uses is correct."""
        # Wavelet reconstruction.
        dwt1 = pywt.upcoef(part="a", coeffs=coeffs[:, 0], wavelet=wavelet_type, level=3)
        dwt2 = pywt.upcoef(
            part="a", coeffs=coeffs[:, 0], wavelet=wavelet_type, level=level
        )
        dwt = dwt2 - dwt1
        theta_dwt = np.vstack((theta_dwt, dwt))

    # Relevant angles.
    theta_dwt = theta_dwt[0: pitch.size]
    # Sinus.
    sin_theta = np.sin(np.deg2rad(theta_dwt))
    # Find peaks in angle, these are posture transitions.
    locs, properties = find_peaks(x=sin_theta, height=0.15, prominance=0.1)
    sin_theta_pks = properties["peak_heights"]

    return locs, sin_theta_pks
