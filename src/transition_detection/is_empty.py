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
                    



    data = pd.read_csv(
        "tests_data/q3_largest.csv", index_col=0, header=None, names=["year", "animal"]
    )
    assert np.all(data.index == largest_species(fname).index)


def test_largest_species_content():
    data = pd.read_csv(
        "tests_data/q3_largest.csv",
        index_col=0,
        header=None,
        names=["year", "animal"],
        squeeze=True,
    )
    assert np.all(data.values == largest_species(fname).values)


def test_assert_lynx_series():
    assert isinstance(lynxes_when_hares(fname), pd.Series)


def test_lynx_idx():
    data = pd.read_csv(
        "tests_data/q3_lynx.csv", index_col=0, header=None, names=["year", "lynx"]
    )
    assert np.all(data.index == lynxes_when_hares(fname).index)


def test_lynx_values():
    data = pd.read_csv(
        "tests_data/q3_lynx.csv",
        index_col=0,
        header=None,
        names=["year", "lynx"],
        squeeze=True,
    )
    assert np.allclose(data.values, lynxes_when_hares(fname).values)