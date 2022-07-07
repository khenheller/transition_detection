import pandas as pd
import numpy as np
import pytest

from src.transition_detection.find_stillness import *

FIND_STILLNESS_TYPEERROR_INPUTS = ["s", 0, None, [], {}, True, "!", 9, pd.DataFrame()]
TYPE_ERROR_INPUTS_FOR_INT = ["S", None, [], {}, "!", pd.DataFrame(), np.array()]

# check if parameter a_mag is not np.array
@pytest.mark.parametrize("a_mag", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(a_mag):
    with pytest.raises(TypeError):
        find_stillness(a_mag, 100, np.array(5))

# check if parameter a_mag is empty
@pytest.mark.parametrize("a_mag", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        find_stillness(np.ndarray((0, 0)))

# check if parameter lying_vec_lumbar is not np.array
@pytest.mark.parametrize("lying_vec_lumbar", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(lying_vec_lumbar):
    with pytest.raises(TypeError):
        find_stillness(np.array(5), 100, lying_vec_lumbar)

# check if parameter lying_vec_lumbar is empty
@pytest.mark.parametrize("lying_vec_lumbar", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror(ying_vec_lumbar):
    with pytest.raises(ValueError):
        find_stillness(np.ndarray((0, 0)))

# check if parameter fs is not int
@pytest.mark.parametrize("fs", TYPE_ERROR_INPUTS_FOR_INT)
def test_invalid_input_raises_typeerror(fs):
        with pytest.raises(TypeError):
            find_stillness(np.array(5), fs, np.array(5))        