import scipy
from scipy import io
import os
from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np


def files_lists(listingAcc_path:str,listingGait_path:str,listingLying_path:str):
    "This function create lists of different measurement situation"
    listing_acc = os.listdir(listingAcc_path)  # list of all the files under ACC folder
    listing_gait = os.listdir(listingGait_path)  # list of all the files under Gait folder
    listing_lying = os.listdir(listingLying_path)  # list of all the files under Lying folder

    listing_lumbar = []
    listing_thigh = []
    for l in listing_acc:  # separate the ACC list to listingLumbar and listingThigh
        if 'lumbar' in l:
            listing_lumbar.append(l)
        else:
            listing_thigh.append(l)

    return listing_acc,listing_gait,listing_lying,listing_lumbar,listing_thigh

