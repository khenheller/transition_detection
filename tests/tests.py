import pytest
import pandas as pd
import numpy as np

from src.transition_detection.preprocessing import *
from src.transition_detection.PT_next_to_lying import *
from src.transition_detection.find_sit_to_stand import *
from src.transition_detection.statistics import *

PREPROCESSING_TYPEERROR_INPUTS = ['s', 0, None, [], {}, True, '!', 9, pd.DataFrame()]
DELETE_PT_NEXT_TO_LYING_TYPEERROR_INPUTS = [(1, 2, 3, 4, 5),
                                            ('s', 'x', True, np.ndarray((0,0)), 'ddd'),
                                            ('s', 'x', True, 2, np.ndarray(range(1, 4))),
                                            (np.ndarray(range(1, 4)), 3, 5, 6, 9),
                                            (False, np.ndarray(range(1, 4)), 'g', pd.DataFrame([1,2,3]), 6),
                                            (np.ndarray(range(1, 4)), 'r', 'g', pd.DataFrame([1,2,3]), 8),
                                            (False, 3, np.ndarray(range(1, 4)), 'g', "66f")
                                            ]

EMPTY_NDARRAY = np.ndarray((0, 0))
NON_EMPTY_NDARRAY = np.ndarray(range(1, 4))

DELETE_PT_NEXT_TO_LYING_VALUEERROR_INPUTS = \
    [(EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, 2),
    (NON_EMPTY_NDARRAY, EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, 2),
(NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, EMPTY_NDARRAY, NON_EMPTY_NDARRAY, 2),
(NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, EMPTY_NDARRAY, 2)
                                             ]

FIND_SIT2STAND_TYPEERROR_INPUTS = ['s', 0, None, [], {}, True, '!', 9, pd.DataFrame()]

PERFORMANCE_DETECTION_TYPEERROR_INPUTS = [
    (1, 2, 3, 4, 5, 6),
    ('s', 'x', True, 6, np.ndarray((0, 0)), 'ddd'),
    ('s', 'x', True, 2, 'g', np.ndarray(range(1, 4))),
    (np.ndarray(range(1, 4)), 2, 3, 5, 6, 9),
    (False, np.ndarray(range(1, 4)), 'g', 3, pd.DataFrame([1, 2, 3]), 6),
    (np.ndarray(range(1, 4)), 'r', 'g', 3, pd.DataFrame([1, 2, 3]), 8),
    (False, True, 3, np.ndarray(range(1, 4)), 'g', "66f")]

PERFORMANCE_DETECTION_VALUEERROR_INPUTS = \
    [(EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, 2),
    (NON_EMPTY_NDARRAY, EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, 2),
    (NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, EMPTY_NDARRAY, NON_EMPTY_NDARRAY,NON_EMPTY_NDARRAY, 2),
    (NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, EMPTY_NDARRAY, NON_EMPTY_NDARRAY, 2),
    (NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, NON_EMPTY_NDARRAY, EMPTY_NDARRAY, 2)]

@pytest.mark.parametrize("lumbar_acc", PREPROCESSING_TYPEERROR_INPUTS)
def test_preprocessing_invalid_input_raises_typeerror(lumbar_acc):
    with pytest.raises(TypeError):
        preprocessing(lumbar_acc)


def test_preprocessing_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        preprocessing(np.ndarray((0, 0)))


@pytest.mark.parametrize("pt, lying_vec_lumbar, ix_stillnes, walking_vec_lumbar, fs", DELETE_PT_NEXT_TO_LYING_TYPEERROR_INPUTS)
def test_delete_pt_next_to_lying_invalid_input_raises_typeerror(pt, lying_vec_lumbar, ix_stillnes, walking_vec_lumbar, fs):
    with pytest.raises(TypeError):
        delete_PT_next_to_lying(pt, lying_vec_lumbar, ix_stillnes, walking_vec_lumbar, fs)


@pytest.mark.parametrize("pt, lying_vec_lumbar, ix_stillnes, walking_vec_lumbar, fs",
                         DELETE_PT_NEXT_TO_LYING_VALUEERROR_INPUTS)
def test_delete_pt_next_to_lying_empty_input_raises_valueerror(pt, lying_vec_lumbar, ix_stillnes, walking_vec_lumbar, fs):
    with pytest.raises(ValueError):
        delete_PT_next_to_lying(pt, lying_vec_lumbar, ix_stillnes, walking_vec_lumbar, fs)


@pytest.mark.parametrize("sitting_vec", FIND_SIT2STAND_TYPEERROR_INPUTS)
def test_find_s2stand_invalid_input_raises_typeerror(sitting_vec):
    with pytest.raises(TypeError):
        find_sit_to_stand(sitting_vec)


def test_find_s2stand_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        find_sit_to_stand(np.ndarray((0, 0)))


@pytest.mark.parametrize("pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs",
                         PERFORMANCE_DETECTION_TYPEERROR_INPUTS)
def test_performance_detection_invalid_input_raises_typeerror(pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs):
    with pytest.raises(TypeError):
        performance_detection(pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs)


@pytest.mark.parametrize("pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs",
                         PERFORMANCE_DETECTION_VALUEERROR_INPUTS)
def test_performance_detection_empty_input_raises_valueerror(pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs):
    with pytest.raises(ValueError):
        performance_detection(pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs)









