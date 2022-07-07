import pandas as pd
import numpy as np
import pytest

from src.transition_detection.elimination2 import *

FIND_STILLNESS_TYPEERROR_INPUTS = ["s", 0, None, [], {}, True, "!", 9, pd.DataFrame()]
TYPE_ERROR_INPUTS_FOR_INT = ["S", None, [], {}, "!", pd.DataFrame(), np.array()]

# check if parameter pt is not np.ndarray
@pytest.mark.parametrize("pt", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(pt):
    with pytest.raises(TypeError):
        elimination2(pt, np.array(5), np.array(5))

# check if parameter pt is empty
@pytest.mark.parametrize("pt", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        elimination2(np.ndarray((0, 0)))

# check if parameter fs is not int
@pytest.mark.parametrize("fs", TYPE_ERROR_INPUTS_FOR_INT)
def test_invalid_input_raises_typeerror(fs):
        with pytest.raises(TypeError):
            elimination2(np.array(5), fs, np.array(5))             