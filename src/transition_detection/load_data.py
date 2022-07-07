import mat73
import os.path
import scipy


def load_data(
    ff: int,
    listing_acc_path: str,
    listing_gait_path: str,
    listing_lying_path: str,
    listing_gait: list,
    listing_lying: list,
    listing_thigh: list,
    listing_lumbar: list,
):
    """The function loads the data, and divides the data to lumbar and thigh acceleration,
    lumbar walking vector and lumbar laying vector,
    thigh walking vector and thigh laying vector.

    Args:
        ff (int): subject index.
        listing_acc_path (str): path of accelerometor file.
        listing_gait_path (str): path of gait file.
        listing_lying_path (str): path of laying file.
        listing_gait (list): name of gate file.
        listing_lying (list): name of laying file.
        listing_thigh (list): name of thigh file.
        listing_lumbar (list): name of lumbar file.

    Raises:
        ValueError: Didn't find file of subject.

    Returns:
        lumbar_acc (np.ndarray): lumbar acceleration data.
        walking_vec_lumbar (np.ndarray): lumbar walking data.
        lying_vec_lumbar (np.ndarray): lumbar laying data.
        thigh_acc (np.ndarray): thigh acceleration data.
        walking_vec_thigh (np.ndarray): thigh walking data.
        laying_vec_thigh (np.ndarray): thigh laying data.
    """
    id_lumbar = listing_lumbar[ff][0:7]  # the ID of lumbar for specific subject
    subject_num = listing_lumbar[ff][-7:-4]
    full_path = os.path.join(
        listing_acc_path, listing_lumbar[ff]
    )  # full path of lumbar ACC file of specific subject
    lumbar_acc = mat73.loadmat(full_path)  # load mat file
    lumbar_acc = lumbar_acc["New_Data"]  # extract the lumbar ACC array

    ix = [l for l in listing_gait if id_lumbar in l]
    if len(ix) >= 1:  # if this data exist for specific subject
        full_path = os.path.join(listing_gait_path, ix[0])
        lumbar_gait = scipy.io.loadmat(full_path)  # extract the lumbar Gait array
        walking_vec_lumbar = lumbar_gait["Walking_Vec"]
    else:
        raise ValueError(f"The lumbar gait file doesnt exist for {subject_num}")

    ix = [l for l in listing_lying if id_lumbar in l]
    if len(ix) >= 1:  # if this data exist for specific subject
        full_path = os.path.join(listing_lying_path, ix[0])
        lumbar_lying = scipy.io.loadmat(full_path)  # extract the lumbar laying array
        lying_vec_lumbar = lumbar_lying["Lying_Vec"]
    else:
        raise ValueError(f"The lumbar lying file doesnt exist for {subject_num}")

    ix = [l for l in listing_thigh if subject_num in l]
    if len(ix) >= 1:  # if this data exist for specific subject
        full_path = os.path.join(listing_acc_path, ix[0])
        thigh_acc = mat73.loadmat(full_path)
        thigh_acc = thigh_acc["New_Data"]
    else:
        raise ValueError(f"The thigh acc file doesnt exist for {subject_num}")

    ix = [l for l in listing_gait if (subject_num in l) & ("thigh" in l)]
    if len(ix) >= 1:  # if this data exist for specific subject
        full_path = os.path.join(listing_gait_path, ix[0])
        thigh_gait = scipy.io.loadmat(full_path)  # extract the thigh Gait array
        walking_vec_thigh = thigh_gait["Walking_Vec"]
    else:
        raise ValueError(f"The thigh gait file doesnt exist for {subject_num}")

    ix = [l for l in listing_lying if (subject_num in l) & ("thigh" in l)]
    if len(ix) >= 1:
        full_path = os.path.join(listing_lying_path, ix[0])
        thigh_lying = scipy.io.loadmat(full_path)  # extract the thigh laying array
        laying_vec_thigh = thigh_lying["Lying_Vec"]
    else:
        raise ValueError(f"The thigh lying file doesnt exist for {subject_num}")

    return (
        lumbar_acc,
        walking_vec_lumbar,
        lying_vec_lumbar,
        thigh_acc,
        walking_vec_thigh,
        laying_vec_thigh,
    )
