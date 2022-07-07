import pandas as pd
import numpy as np
import scipy.signal
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
from src.transition_detection.test_types import *

def preprocessing(lumbar_acc: np.ndarray):
    """
    The function filters the lumbar data via low pass filter, and divides the data to accelerometer and gyroscope values

    :param listingLumbar: DataFrame, accelerometer data on 3 axis, on multiple time points
    :return:
    """
    test_types([lumbar_acc], ["lumbar_acc"], [np.ndarray])

    fs = 100  # SampleRate
    n = 4  # filter order
    fc = 5  # cutoff frequency
    b, a = scipy.signal.butter(n, fc, btype='low', analog=False, fs=fs)  # design filter
    data = scipy.signal.filtfilt(b, a, lumbar_acc, padlen=0)  # apply filter to data

    acc = data[:, 0:3] * 9.81  # take only accelerometer values and add gravity impact ?
    v = acc[:, 0]
    ml = acc[:, 1]
    ap = acc[:, 2]

    gyro = data[:, 3:6]   #take only gyroscope values
    yaw = acc[:, 0]
    pitch = acc[:, 1]
    roll = acc[:, 2]

    a_mag = np.sqrt(v ** 2 + ap ** 2 + ml ** 2)  # Magnitude
    # g_mag = np.sqrt(yaw**2 + pitch**2 + roll ** 2);

    print("returning from preprocessing")
    return (
        {'acc': acc, 'v': v, 'ml': ml, 'ap': ap},
        {'gyro': gyro, 'yaw': yaw, 'pitch': pitch, 'roll': roll},
        {'magnitude': a_mag, 'fs': fs}
    )




