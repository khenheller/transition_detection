# elimination2
import pandas as pd
import numpy as np
import re
from os.path import dirname, join as pjoin
import scipy.io
from is_empty import *
from test_types import *

def elimination2(
    pt: np.ndarray,
    fs: int,
):
    """_summary_

    Args:
        pt (np.ndarray): posture transition array.
        fs (int): Sample rate.

    Returns:
        np.ndarray: postural changes.
    """
    test_types([pt, fs], ["pt", "fs"], [np.ndarray,int])
    is_empty([pt, fs], ["pt", "fs"])


    delete_pt = []
    ind1 = []
    for i in range(len(pt) - 1):
        x = [pt[i, 1], pt[i + 1, 1]]
        if x == [1, 2]:
            ind1.append(i)

    for jj in range(len(ind1)):
        segment_length = len(np.arange(pt[ind1[jj], 0], pt[ind1[jj] + 1, 0], 1))
        if segment_length < 10 * fs:
            delete_pt = [[delete_pt], [ind1[jj]], [ind1[jj] + 1]]
    pt[delete_pt, :] = [] * len(delete_pt)
    return pt
