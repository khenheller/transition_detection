import os
from os.path import dirname, join as pjoin


INVALID_INPUT_MESSAGE = 'Invalid input: {path}'

def files_lists(listing_acc_path:str,listing_gait_path:str,listing_lying_path:str):

    """ This function create lists of different measurement situation

        Parameters
        ----------
        listing_acc_path: path of the 3D gyroscopes and 3D accelerometers files
        listing_gait_path:  path of the gait files
        listing_lying_path: path of the lying files

        Returns
        -------
        listing_acc: list of all the acc mat files
        listing_gait: list of all the gait mat files
        listing_lying: list of all the lying mat files
        listing_lumbar: acc lumbar mat files
        listing_thigh: acc thigh mat files

    """
    #For the listing_acc_path
    if not os.path.isdir(listing_acc_path):  # missing folder
        message = INVALID_INPUT_MESSAGE.format(path=listing_acc_path)
        raise ValueError(message)

    if isinstance(listing_acc_path, str):
        listing_acc = os.listdir(listing_acc_path)  # list of all the files under ACC folder


    #For the listing_gait_path
    if not os.path.isdir(listing_gait_path):  # missing folder
        message = INVALID_INPUT_MESSAGE.format(path=listing_gait_path)
        raise ValueError(message)

    if isinstance(listing_gait_path, str):
        listing_gait = os.listdir(listing_gait_path)  # list of all the files under Gait folder

    if not os.path.isdir(listing_gait_path):  # missing folder
        message = INVALID_INPUT_MESSAGE.format(path=listing_gait_path)
        raise ValueError(message)


    #For the listing_lying_path
    if not os.path.isdir(listing_lying_path):  # missing folder
        message = INVALID_INPUT_MESSAGE.format(path=listing_lying_path)
        raise ValueError(message)

    if isinstance(listing_lying_path, str):
        listing_lying = os.listdir(listing_lying_path)  # list of all the files under Lying folder

    listing_lumbar = []
    listing_thigh = []

    for l in listing_acc:  # separate the ACC list to listingLumbar and listingThigh
        if ('lumbar' in l) | ('Lumbar' in l): #add the lumbar files to listing_lumbar
            listing_lumbar.append(l)
        else:
            listing_thigh.append(l) #add the thigh files to listing_thigh


    return listing_acc, listing_gait, listing_lying, listing_lumbar, listing_thigh


