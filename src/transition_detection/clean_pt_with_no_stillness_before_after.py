# Clean PT with no stillness before/after
import pandas as pd
import numpy as np
import bottleneck as bn
from is_empty import *
from test_types import *

def clean_pt(
    locs: np.ndarray,
    ix_stillnes:np.ndarray,
    fs: int,
    s_start_pt:np.ndarray,
    s_end_pt:np.ndarray
    ):
    """ Clean PT with no stillness before/after.
    Parameters
    ----------
    locs: array of the location of the transiotions

    Returns
    -------
    locs:clean array of the location of the transiotions
    """

    test_types([locs, ix_stillnes,fs, s_start_pt, s_end_pt], ["locs", "ix_stillnes", "fs", "s_start_pt", "s_end_pt"], [np.ndarray,np.ndarray, int, np.ndarray,np.ndarray])
    is_empty_input([locs, ix_stillnes,fs, s_start_pt, s_end_pt], ["locs", "ix_stillnes", "fs", "s_start_pt", "s_end_pt"])



    delete_locs = []
    for ii in range(len(locs)):
        try:
            still_before_mat= ix_stillnes[np.arange(locs[ii]-15*fs, locs[ii],1)]
            still_before = (still_before_mat.sum(axis=0))/(15*fs)
            still_after_mat = ix_stillnes[np.arange(locs[ii]+1, locs[ii]+15*fs+1,1)]
            still_after = (still_after_mat.sum(axis=0))/(15*fs)
            if np.logical_and(still_before < 0.5, still_after < 0.5):
                delete_locs = [[delete_locs],[ii]]
                continue
        except:
            print("An exception occurred")  
        c = np.intersect1d([np.arange(locs[ii]-15*fs, locs[ii]+15*fs+1, 1)],[[s_start_pt],[s_end_pt]]) # Return the sorted, unique values that are in both of the input arrays.
        if not np.any(c):
            delete_locs = [[delete_locs],[ii]]
            continue
            
    locs[delete_locs] = []  
    return locs
