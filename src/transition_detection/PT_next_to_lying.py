import numpy as np
import re
from test_types import *
from is_empty import *

def delete_PT_next_to_lying(pt: np.ndarray, lying_vec_lumbar: np.ndarray, ix_stillness: np.ndarray,
                            walking_vec_lumbar: np.ndarray, fs: int = 100):
    """
    Delete PT next to lying segments

    :param pt: posture transition array
    :param lying_vec_lumbar: binary vector indicating walking state according to lumbar sensor
    :param ix_stillness:
    :param walking_vec_lumbar: binary vector indicating walking state according to lumbar sensor
    :param fs: sample rate
    :return:
    pt: posture transition array after deletion of PT's next to lying segments
    """
    test_types([pt, lying_vec_lumbar, ix_stillness, walking_vec_lumbar, fs],
               ["pt", "lying_vec_lumbar", "ix_stillness", "walking_vec_lumbar", "fs"],
               [np.ndarray, np.ndarray, np.ndarray, np.ndarray, int])
    is_empty([pt, lying_vec_lumbar, ix_stillness, walking_vec_lumbar, fs],
               ["pt", "lying_vec_lumbar", "ix_stillness", "walking_vec_lumbar", "fs"])

    delete_pt = []  # indices of PTs to delete- empty
    for jj in np.ndarray(range(1, len(pt[:, 0]))):
        if sum(lying_vec_lumbar[pt[jj, 0] - 15 * fs : pt[jj, 0] + 15*fs]) > 0:
            delete_pt.append(jj)  # add PT to deletion vector

    pt[delete_pt, :] = []  # delete PTs

    #ind1 = [m.start() for m in re.finditer([1, 1], pt[:, 1].T)]
    ind1 = []
    for i in range(len(pt) - 1):
        x = [pt[i, 1], pt[i + 1, 1]]
        if x == [1, 1]:
            ind1.append(i)

    delete_pt = []
    while ind1:
        for jj in np.ndarray(range(1, len(ind1))):
            stillness = sum(ix_stillness[pt[ind1[jj], 0]: pt[ind1[jj] + 1, 0]]) / len(
                ix_stillness[pt[ind1[jj], 0]:pt[ind1[jj] + 1, 0]])
            walking = sum(walking_vec_lumbar[pt[ind1[jj], 0]: pt[ind1[jj] + 1, 0]]) / len(
                walking_vec_lumbar[pt[ind1[jj], 0]:pt[ind1[jj] + 1, 0]])
            if stillness < 0.85 or walking > 0.05:
                delete_pt.append(ind1[jj] + 1)
            else:
                delete_pt.append(ind1[jj])
            delete_pt = np.unique(delete_pt)  # delete duplicates & sort
        pt[delete_pt, :] = []  # delete PTs
        delete_pt = []  # empty deletion vector
        #ind1 = [m.start() for m in re.finditer([1, 1], pt[:, 1].T)]  # reset
        ind1 = []
        for i in range(len(pt) - 1):
            x = [pt[i, 1], pt[i + 1, 1]]
            if x == [1, 1]:
                ind1.append(i)

    return pt
