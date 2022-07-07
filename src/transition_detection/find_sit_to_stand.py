import numpy as np


def find_sit_to_stand(sitting_vec: np.ndarray):
    """
    The function finds transitions from sit to stand and return the indices of transitions
    
    :param sitting_vec: thigh signal used to detect sitting and standing postures
    :return:
    s2sit_index: indices of transitions from stand to sit
    s2stand_index: indices of transitions from sit to stand
    """
    s2sit_index = np.argwhere(diff(sitting_vec) == 1)  # find sitting according to thigh signal
    s2stand_index = np.argwhere(diff(sitting_vec) == -1)  # find standing according to thigh signal
    
    if len(s2stand_index) > len(s2sit_index):  # transitions from sit to stand.
        s2stand_index[0]= []
    elif len(s2sit_index) > len(s2stand_index):
        s2sit_index[-1] = []
        
    if s2sit_index[0] > s2stand_index[0]:
        s2stand_index[0] = []
        s2sit_index[-1] = []
        
    return s2sit_index, s2stand_index

