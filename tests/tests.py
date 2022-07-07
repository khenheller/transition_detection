import pytest
import pandas as pd
import numpy as np

from preprocessing.py import *

PREPROCESSING_TYPEERROR_INPUTS = ['s', 0, None, [], {}, True, '!', 9, pd.DataFrame()]

@pytest.mark.parametrize("lumbar_acc", PREPROCESSING_TYPEERROR_INPUTS)
def test_preprocessing_invalid_input_raises_typeerror(lumbar_acc):
    with pytest.raises(TypeError):
        preprocessing(lumbar_acc)


def test_preprocessing_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        preprocessing(np.ndarray((0, 0)))










