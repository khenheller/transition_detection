import pandas as pd
import numpy as np
import pytest

from src.transition_detection.elimination1 import *

FIND_STILLNESS_TYPEERROR_INPUTS = ["s", 0, None, [], {}, True, "!", 9, pd.DataFrame()]

# check if parameter pt is not np.ndarray
@pytest.mark.parametrize("pt", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(pt):
    with pytest.raises(TypeError):
        elimination1(pt, np.array(5), np.array(5))

# check if parameter pt is empty
@pytest.mark.parametrize("pt", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        elimination1(np.ndarray((0, 0)))

# check if parameter ix_stillnes is not np.ndarray
@pytest.mark.parametrize("ix_stillness", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(ix_stillness):
    with pytest.raises(TypeError):
        elimination1( np.array(5), ix_stillness, np.array(5))

# check if parameter ix_stillnes is empty
@pytest.mark.parametrize("ix_stillness", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        elimination1(np.ndarray((0, 0)))     

# check if parameter walking_vec_lumber is not np.ndarray
@pytest.mark.parametrize("walking_vec_lumber", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(walking_vec_lumber):
    with pytest.raises(TypeError):
        elimination1( np.array(5),  np.array(5), walking_vec_lumber)

# check if parameter walking_vec_lumber is empty
@pytest.mark.parametrize("walking_vec_lumber", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        elimination1(np.ndarray((0, 0)))             