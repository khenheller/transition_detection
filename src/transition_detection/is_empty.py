import pandas as pd
import numpy as np
import pytest
from collections.abc import Iterable



def is_empty_input(var_list: list, var_name_list: list):
    """Checks if all iterables vars are not empty
    Args:
        var_list (list): vars to check
        var_name_list (list): var names as char or string
    Raises:
        TypeError: One of the vars has the wrong type
    """
    for var, name in zip(var_list, var_name_list):
        if isinstance(name, Iterable):
            if type(name) == np.ndarray:
                if name.size==0:
                    raise TypeError(f"The var {name} from the type {type(name)} is empty")
            else:
                if len(name) == 0:
                    raise TypeError(f"The var {name} from the type {type(name)} is empty")
    