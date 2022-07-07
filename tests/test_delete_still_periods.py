import pandas as pd
import numpy as np
import pytest

from src.transition_detection.delete_still_periods import *

FIND_STILLNESS_TYPEERROR_INPUTS = ["s", 0, None, [], {}, True, "!", 9, pd.DataFrame()]
TYPE_ERROR_INPUTS_FOR_INT = ["S", None, [], {}, "!", pd.DataFrame(), np.array()]

# check if parameter s2sit_index is not np.array
@pytest.mark.parametrize("s2sit_index", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(s2sit_index):
    with pytest.raises(TypeError):
        delete_still_periods(s2sit_index, np.array(5),  np.array(5), np.array(5), np.array(5),100)

# check if parameter s2sit_index is empty
@pytest.mark.parametrize("s2sit_index", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        delete_still_periods(np.ndarray((0, 0)))

# check if parameter walking_vec_lumbar is not np.array
@pytest.mark.parametrize("walking_vec_lumbar", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(walking_vec_lumbar):
    with pytest.raises(TypeError):
        delete_still_periods(np.array(5), walking_vec_lumbar, np.array(5), np.array(5), np.array(5),100)

# check if parameter walking_vec_lumbar is empty
@pytest.mark.parametrize("walking_vec_lumbar", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        delete_still_periods(np.ndarray((0, 0)))        

# check if parameter s2stand_index is not np.array
@pytest.mark.parametrize("s2stand_index", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(s2stand_index):
    with pytest.raises(TypeError):
        delete_still_periods(np.array(5), np.array(5), s2stand_index,  np.array(5), np.array(5),100)

# check if parameter s2stand_index is empty
@pytest.mark.parametrize("s2stand_index", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        delete_still_periods(np.ndarray((0, 0)))            

# check if parameter ix_stillnes is not np.array
@pytest.mark.parametrize("ix_stillnes", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(ix_stillnes):
    with pytest.raises(TypeError):
        delete_still_periods(np.array(5), np.array(5), np.array(5), ix_stillnes, np.array(5),100)

# check if parameter ix_stillnes is empty
@pytest.mark.parametrize("ix_stillnes", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        delete_still_periods(np.ndarray((0, 0))) 

# check if parameter lying_vec_lumbar is not np.array
@pytest.mark.parametrize("lying_vec_lumbar", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_invalid_input_raises_typeerror(lying_vec_lumbar):
    with pytest.raises(TypeError):
        delete_still_periods(np.array(5), np.array(5), np.array(5), np.array(5), lying_vec_lumbar, 100)

# check if parameter lying_vec_lumbar is empty
@pytest.mark.parametrize("lying_vec_lumbar", FIND_STILLNESS_TYPEERROR_INPUTS)
def test_empty_input_raises_valueerror():
    with pytest.raises(ValueError):
        delete_still_periods(np.ndarray((0, 0)))


# check if parameter fs is not int
@pytest.mark.parametrize("fs", TYPE_ERROR_INPUTS_FOR_INT)
def test_invalid_input_raises_typeerror(fs):
        with pytest.raises(TypeError):
            delete_still_periods(np.array(5), fs, np.array(5))                                                            