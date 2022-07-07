import pandas as pd
import numpy as np
import pytest

from src.transition_detection.clean_pt_with_no_stillness_before_after import *

FIND_STILLNESS_TYPEERROR_INPUTS = ["s", 0, None, [], {}, True, "!", 9, pd.DataFrame()]
TYPE_ERROR_INPUTS_FOR_INT = ["S", None, [], {}, "!", pd.DataFrame(), np.array()]

# check if parameter locs is not np.array
@pytest.mark.parametrize("locs", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(locs):
    with pytest.raises(TypeError):
        clean_pt(locs, np.array(5), 100, np.array(5), np.array(5))

# check if parameter locs is empty
@pytest.mark.parametrize("locs", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        clean_pt(np.ndarray((0, 0)))

# check if parameter ix_stillnes is not np.array
@pytest.mark.parametrize("ix_stillnes", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(ix_stillnes):
    with pytest.raises(TypeError):
        clean_pt(np.array(5), ix_stillnes,  100, np.array(5), np.array(5))

# check if parameter ix_stillnes is empty
@pytest.mark.parametrize("ix_stillnes", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror(ix_stillnes):
    with pytest.raises(ValueError):
        clean_pt(np.ndarray((0, 0)))

# check if parameter fs is not int
@pytest.mark.parametrize("fs", TYPE_ERROR_INPUTS_FOR_INT)
def test_invalid_input_raises_typeerror(fs):
        with pytest.raises(TypeError):
            clean_pt(np.array(5), fs, np.array(5))        


# check if parameter s_start_pt is not np.array
@pytest.mark.parametrize("s_start_pt", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(s_start_pt):
    with pytest.raises(TypeError):
        clean_pt(np.array(5), np.array(5), 100, s_start_pt, np.array(5))

# check if parameter s_start_pt is empty
@pytest.mark.parametrize("s_start_pt", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        clean_pt(np.ndarray((0, 0)))

# check if parameter s_end_pt is not np.array
@pytest.mark.parametrize("s_end_pt", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(s_end_pt):
    with pytest.raises(TypeError):
        clean_pt(np.array(5), np.array(5), 100, np.array(5), s_end_pt)

# check if parameter s_end_pt is empty
@pytest.mark.parametrize("s_end_pt", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror(s_end_pt):
    with pytest.raises(ValueError):
        clean_pt(np.ndarray((0, 0)))            