import numpy as np
from test_types import *
from is_empty import *

# import scipy.io
# pt = scipy.io.loadmat('pt.mat')
# pt = pt['PT']
# s2sit_index = scipy.io.loadmat('s2sit_index.mat')
# s2sit_index = s2sit_index['s2sit_index']
# s2stand_index = scipy.io.loadmat('s2stand.mat')
# s2stand_index = s2stand_index['s2stand_index']

def performance_detection(pt: np.ndarray, s2sit_index: np.ndarray, s2stand_index: np.ndarray,
                          ix_stillness: np.ndarray, lying_vec_lumbar: np.ndarray, sitting_vec: np.ndarray, fs: int):
    """
    The function calculate precision, sensitivity and accuracy of transitions detection from
    lumbar sensors, compared to detection using both lumbar and thigh sensors.
    The function prints the values mentioned above.

    :param pt: posture transition array
    :param s2sit_index: indices of transitions from stand to sit
    :param s2stand_index: indices of transitions from sit to stand
    :param ix_stillness: indices of stillness periods
    :param lying_vec_lumbar: binary vector indicating walking state according to lumbar sensor
    :param sitting_vec:
    :param fs: sample rate
    :return:

    s2sit_sensitivity: sensitivity of stand-to-sit detection
    s2sit_precision: precision of stand-to-sit detection
    s2stand_sensitivity: sensitivity of sit-to-stand detection
    s2stand_precision: precision of sit-to-stand detection
    sitting_acc: accuracy of total sitting time
    """

    test_types([pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs],
               ["pt", "s2sit_index", "s2stand_index", "ix_stillness", "lying_vec_lumbar", "sitting_vec", "fs"],
               [np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, int])
    is_empty([pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs],
               ["pt", "s2sit_index", "s2stand_index", "ix_stillness", "lying_vec_lumbar", "sitting_vec", "fs"])

    pt_s2sit = pt[pt[:, 1] == 2, 0]  # posture transitions from stand to sit
    pt_s2stand = pt[pt[:, 1] == 1, 0]  # posture transitions from sit to stand

    # initiate stand to sit counters
    tp_s2sit = 0  # true positive
    fp_s2sit = 0  # false positive
    fn_s2sit = 0  # false negative

    # initiate sit to stand counters
    tp_s2stand = 0  # true positive
    fp_s2stand = 0  # false positive
    fn_s2stand = 0  # false negative

    # classify stand to sit transitions
    for i in range(0, len(pt_s2sit)):
        if np.any(np.isin(s2sit_index, np.arange(pt_s2sit[i] - 15 * fs, pt_s2sit[i] + 15 * fs))):
            tp_s2sit = tp_s2sit + 1  # count true positive
        else:
            fp_s2sit = fp_s2sit + 1  # count false positive

    for i in range(0, len(s2sit_index)):
        # if not np.any(np.isin(pt_s2sit, np.arange(s2sit_index[0][i] - 15 * fs, s2sit_index[0][i] + 15 * fs))):
        if not np.any(np.isin(pt_s2sit, np.arange(s2sit_index[i] - 15 * fs, s2sit_index[i] + 15 * fs))):
            fn_s2sit = fn_s2sit + 1

    # classify sit to stand transitions
    for i in range(0, len(pt_s2stand)):
        if np.any(np.isin(s2stand_index, np.arange(pt_s2stand[i] - 15 * fs, pt_s2stand[i] + 15 * fs))):
            tp_s2stand = tp_s2stand + 1  # count true positive
        else:
            fp_s2stand = fp_s2stand + 1  # count false positive

    for i in range(0, len(s2stand_index)):
        # if not np.any(np.isin(pt_s2stand, np.arange(s2stand_index[0][i] - 15 * fs, s2stand_index[0][i] + 15 * fs))):
        if not np.any(np.isin(pt_s2stand, np.arange(s2stand_index[i] - 15 * fs, s2stand_index[i] + 15 * fs))):
            fn_s2stand = fn_s2stand + 1

    # performance evaluation
    s2sit_sensitivity = tp_s2sit / (tp_s2sit + fn_s2sit) * 100  # calculate sensitivity of stand to sit detection
    s2sit_precision = tp_s2sit / (tp_s2sit + fp_s2sit) * 100  # calculate precision of stand to sit detection
    print(f"Stand to sit sensitivity: {s2sit_sensitivity} \nStand to sit precision: {s2sit_precision}")

    s2stand_sensitivity = tp_s2stand/(tp_s2stand + fn_s2stand) * 100 # calculate sensitivity of sit to stand detection
    s2stand_precision = tp_s2stand/(tp_s2stand + fp_s2stand) * 100  # calculate precision of sit to stand detection
    print(f"Sit to stand sensitivity: {s2stand_sensitivity} \nSit to stand precision: {s2stand_precision}")

    ix_sitting = np.zeros(ix_stillness.shape())
    for k in range(0, len(pt_s2sit)):
        ix_sitting[pt_s2sit[k]: pt_s2stand[k]] = 1
    ix_sitting[lying_vec_lumbar == 1] = 0  # reset sitting indices where lumbar sensor detected lying
    sitting_acc = sum(ix_sitting) / sum(sitting_vec) * 100  # accuracy of total sitting time
    print(f"Accuracy of total sitting time: {sitting_acc}")

    return s2sit_sensitivity, s2sit_precision, s2stand_sensitivity, s2stand_precision, sitting_acc

# performance_detection(pt, s2sit_index, s2stand_index, [], [], [], 100)