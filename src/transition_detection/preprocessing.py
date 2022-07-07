import pandas as pd
import numpy as np
import scipy.signal


def preprocessing(listingLumbar: pd.DataFrame):
    """The functions filters the lumbar data via lowpass filter, and divides the data
    to acceleromotor and gyroscope values.

    Args:
        listingLumbar (pd.DataFrame): Acceleromotr data on 3 axis, on multiple timepoints.

    Returns:
        dict: 3 dictioneris, one for params related to acc, one for params related to gyro
        and one for params relted to magnitude.
    """

    fs = 100  # SampleRate
    n = 4  # filter order
    fc = 5  # cutoff frequency
    b, a = scipy.signal.butter(n, fc, btype="low", analog=False, fs=fs)  # design filter
    data = scipy.signal.filtfilt(b, a, listingLumbar, padlen=0)  # apply filter to data

    acc = data[:, 0:3] * 9.81  # take only accelerometer values and add gravity impact ?
    v = acc[:, 0]
    ml = acc[:, 1]
    ap = acc[:, 2]

    gyro = data[:, 3:6]  # take only gyroscope values
    yaw = acc[:, 0]
    pitch = acc[:, 1]
    roll = acc[:, 2]

    a_mag = np.sqrt(v**2 + ap**2 + ml**2)  # Magnitude
    # g_mag = np.sqrt(yaw**2 + pitch**2 + roll ** 2);

    return (
        {"acc": acc, "v": v, "ml": ml, "ap": ap},
        {"gyro": gyro, "yaw": yaw, "pitch": pitch, "roll": roll},
        {"magnitude": a_mag, "fs": fs},
    )
