# delete_still_periods
import pandas as pd
import numpy as np
import bottleneck as bn

def delete_still_periods(
    s2sit_index: None,
    walking_vec_lumbar: np.ndarray,
    s2stand_index: None,
    ix_stillnes: None,
    lying_vec_lumbar: np.ndarray,
    fs:int
    ):
    """ 
    Delete still periods that has more than 10% gait detection in it (including driving) +
    Detect still periods above 5min (but not lying) and mark them as sitting (can't be standing)

    Parameters
    ----------
    s2sit_index:
    walking_vec_lumbar:
    s2stand_index:
    ix_stillnes:
    lying_vec_lumbar:
    fs: sample rate

    Returns
    -------
    sitting_vec: binar araay, 1 = sitting, 0 = not sitting 
    """
    # Delete still periods that has more than 10% gait detection in it (including driving)
    delete_ind = []
    for i in range(len(s2sit_index)):
        val_walking = walking_vec_lumbar[range(s2sit_index[i], s2stand_index[i])]
        walking = val_walking.sum(axis = 0) / len(val_walking)
        if walking > 0/1:
            delete_ind = [[delete_ind], [i]]
    s2sit_index[delete_ind] = []
    s2stand_index[delete_ind] = []

# Detect still periods above 5min (but not lying) and mark them as sitting (can't be standing)
    delete_ind = []
    for jj in range(len((s2sit_index)-1)):
        sig_ind = range(s2stand_index[jj], s2sit_index[jj+1])
        stillness = ix_stillnes[sig_ind].sum(axis = 0) / len(sig_ind)
        walking = walking_vec_lumbar[sig_ind].sum(axis=0) / len(sig_ind)
        lying =  lying_vec_lumbar[sig_ind].sum(axis=0) / len(sig_ind)
        if np.logical_and(np.logical_and(len(sig_ind) < 5*60*fs, np.logical_and(stillness > 0.95,walking ==0)), lying == 0):
            delete_ind = [[delete_ind] , [jj]]
        if len(sig_ind) < 10*fs:  # delete standing segments shorter than 10 sec between PTs
            delete_ind = [[delete_ind] , [jj]]
        if lying > 0: # delete false sitting periods that are actually lying    
            delete_ind = [[delete_ind] , [jj]]
    s2stand_index[delete_ind] = []
    s2sit_index[delete_ind] = []        

    sitting_vec = np.zeros(np.shape(sitting_vec))
    for k in len(s2sit_index):
        sitting_vec[s2sit_index[k] : s2stand_index[k]] = 1*(s2stand_index[k] - s2sit_index[k])
    sitting_vec[lying_vec_lumbar == 1] = 0   

    return sitting_vec