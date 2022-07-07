import pytest
import pandas as pd
import numpy as np
from src.transition_detection.find_pt_with_theta import find_pt_with_theta
from src.transition_detection.preprocessing import preprocessing
from transition_detection.pt_detection import pt_detection

np_array = np.array([1, 2, 3])
PREPROCESSING_TYPEERROR_INPUTS = ["s", 0, None, [], {}, True, "!", 9, pd.DataFrame()]


@pytest.mark.parametrize("lumbar_acc", PREPROCESSING_TYPEERROR_INPUTS)
def test_preprocessing_invalid_input_raises_typeerror(lumbar_acc):
    with pytest.raises(TypeError):
        preprocessing(lumbar_acc)


def test_preprocessing_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        preprocessing(np.ndarray((0, 0)))


FIND_PT_WITH_THETA_TYPEERROR_INPUTS = [
    ("s", 100),
    (None, 100),
    ([], 100),
    ({}, 100),
    (True, 100),
    (np.array([1, 2, 3]), "s"),
    (np.array([1, 2, 3]), None),
    (np.array([1, 2, 3]), []),
    (np.array([1, 2, 3]), {}),
    (np.array([1, 2, 3]), True),
]

FIND_PT_WITH_THETA_EMPTYERROR_INPUTS = [(np.ndarray(0), 100)]


@pytest.mark.parametrize("pitch, fs", FIND_PT_WITH_THETA_TYPEERROR_INPUTS)
def test_find_pt_with_theta_invalid_input_raises_typeerror(pitch, fs):
    with pytest.raises(TypeError):
        find_pt_with_theta(pitch, fs)


@pytest.mark.parametrize("pitch, fs", FIND_PT_WITH_THETA_TYPEERROR_INPUTS)
def test_find_pt_with_theta_empty_input_raises_valueerror(pitch, fs):
    with pytest.raises(ValueError):
        find_pt_with_theta(pitch, fs)


def test_find_pt_with_theta_nan_input_raises_valueerror(pitch, fs):
    with pytest.raises(ValueError):
        find_pt_with_theta(np.array([1, 2, 3, np.NaN, 6, 7], 100))


FIND_PT_WITH_THETA_TYPEERROR_INPUTS = [
    ("s", 100, np_array, np_array, np_array, np_array),
    (123, 100, np_array, np_array, np_array, np_array),
    ([], 100, np_array, np_array, np_array, np_array),
    (np_array, "s", np_array, np_array, np_array, np_array),
    (np_array, {}, np_array, np_array, np_array, np_array),
    (np_array, [], np_array, np_array, np_array, np_array),
    (np_array, 100, "s", np_array, np_array, np_array),
    (np_array, 100, 123, np_array, np_array, np_array),
    (np_array, 100, [], np_array, np_array, np_array),
    (np_array, 100, np_array, "s", np_array, np_array),
    (np_array, 100, np_array, 123, np_array, np_array),
    (np_array, 100, np_array, [], np_array, np_array),
    (np_array, 100, np_array, np_array, "s", np_array),
    (np_array, 100, np_array, np_array, 123, np_array),
    (np_array, 100, np_array, np_array, [], np_array),
    (np_array, 100, np_array, np_array, np_array, "s"),
    (np_array, 100, np_array, np_array, np_array, 123),
    (np_array, 100, np_array, np_array, np_array, []),
]

FIND_PT_WITH_THETA_EMPTYERROR_INPUTS = [
    (np.ndarray(0), 100, np_array, np_array, np_array, np_array),
    (np_array, 100, np.ndarray(0), np_array, np_array, np_array),
    (np_array, 100, np_array, np.ndarray(0), np_array, np_array),
    (np_array, 100, np_array, np_array, np.ndarray(0), np_array),
    (np_array, 100, np_array, np_array, np_array, np.ndarray(0)),
]


@pytest.mark.parametrize(
    "locs, fs, acc, gyro, pitch, sin_theta_pks", FIND_PT_WITH_THETA_TYPEERROR_INPUTS
)
def test_pt_detection_invalid_input_raises_typeerror(
    locs, fs, acc, gyro, pitch, sin_theta_pks
):
    with pytest.raises(TypeError):
        pt_detection(locs, fs, acc, gyro, pitch, sin_theta_pks)


@pytest.mark.parametrize(
    "locs, fs, acc, gyro, pitch, sin_theta_pks", FIND_PT_WITH_THETA_TYPEERROR_INPUTS
)
def test_pt_detection_empty_input_raises_valueerror(
    locs, fs, acc, gyro, pitch, sin_theta_pks
):
    with pytest.raises(ValueError):
        pt_detection(locs, fs, acc, gyro, pitch, sin_theta_pks)


def test_pt_detection_epoch_too_big_raises_exception(np_array):
    with pytest.raises(Exception):
        pt_detection(np.array(-1000), 100, np_array, np_array, np_array, np_array)
