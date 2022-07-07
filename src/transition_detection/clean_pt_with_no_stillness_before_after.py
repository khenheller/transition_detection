# Clean PT with no stillness before/after
import pandas as pd
import numpy as np
import bottleneck as bn

def clean_pt(
    locs: np.ndarray,
    ix_stillnes:np.ndarray,
    fs: int,
    s_start_pt:None,
    s_end_pt:None
    ):
    """ Clean PT with no stillness before/after.
    Parameters
    ----------
    locs: array of the location of the transiotions

    Returns
    -------
    locs:clean array of the location of the transiotions
    """
    delete_locs = []
    for ii in range(len(locs)):
        try:
            still_before_mat= ix_stillnes[range(locs[ii]-15*fs, locs[ii])]
            still_before = (still_before_mat.sum(axis=0))/(15*fs)
            still_after_mat = ix_stillnes[range(locs[ii]+1, locs[ii]+15*fs+1)]
            still_after = (still_after_mat.sum(axis=0))/(15*fs)
            if still_before < 0.5 and still_after < 0.5:
                delete_locs = [[delete_locs],[ii]]
                continue
        except:
            print("An exception occurred")    # ???????????
        c = np.intersect1d([range(locs[ii]-15*fs,locs[ii]+15*fs+1)],[[s_start_pt],[s_end_pt]])
        if not np.any(c):
            delete_locs = [[delete_locs],[ii]]
            continue
    locs[delete_locs] = []

    return locs
            

    
