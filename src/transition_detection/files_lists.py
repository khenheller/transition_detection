import scipy
from scipy import io
import os
from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np


def files_lists(listingAcc_path:str,listingGait_path:str,listingLying_path:str):
    "This function create lists of different measurement situation"
    listingAcc = os.listdir(listingAcc_path)  # list of all the files under ACC folder
    listingGait = os.listdir(listingGait_path)  # list of all the files under Gait folder
    listingLying = os.listdir(listingLying_path)  # list of all the files under Lying folder

    listingLumbar = []
    listingThigh = []
    for l in listingAcc:  # separate the ACC list to listingLumbar and listingThigh
        if 'lumbar' in l:
            listingLumbar.append(l)
        else:
            listingThigh.append(l)

    return listingAcc,listingGait,listingLying,listingLumbar,listingThigh

