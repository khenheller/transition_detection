from src.transition_detection.files_lists import files_lists
from src.transition_detection.load_data import load_data
from src.transition_detection.preprocessing import preprocessing
from src.transition_detection.find_stillness import find_stillness
from src.transition_detection.find_pt_with_theta import find_pt_with_theta
from src.transition_detection.clean_pt_with_no_stillness_before_after import clean_pt
from src.transition_detection.pt_detection import pt_detection
from src.transition_detection.PT_next_to_lying import delete_PT_next_to_lying
from src.transition_detection.elimination1 import elimination1
from src.transition_detection.sitting_segements_fitting_standards import sitting_segements_fitting_standards
from src.transition_detection.find_sit_to_stand import find_sit_to_stand
from src.transition_detection.statistics import performance_detection
from src.transition_detection.elimination2 import elimination2
from src.transition_detection.delete_still_periods import delete_still_periods
import numpy as np

def transition_detection(listing_acc_path: str, listing_gait_path: str, listing_lying_path: str):
    """ Transition_detection
        Parameters
        ----------
        listing_acc_path: path of the 3D gyroscopes and 3D accelerometers files
        listing_gait_path:  path of the gait files
        listing_lying_path: path of the lying files

        Returns
        -------
        pt: posture transition array
        s2sit_sensitivity: detection sensitivity for stand-to-sit transitions
        s2sit_precision: detection precision for stand-to-sit transitions
        s2stand_sensitivity: detection sensitivity for sit-to-stand transitions
        s2stand_precision: detection precision for sit-to-stand transitions
    """


    #Create files lists
    (listing_acc, listing_gait, listing_lying, listing_lumbar, listing_thigh)= files_lists(listing_acc_path, listing_gait_path, listing_lying_path)
    fs = 100  # sample rate

    for ff in range(len(listing_lumbar)): #for each subject

        #load the data (1-18)
        (lumbar_acc, walking_vec_lumbar, lying_vec_lumbar, thigh_acc, walking_vec_thigh, laying_vec_thigh) = load_data(ff, listing_acc_path, listing_gait_path, listing_lying_path, listing_acc,listing_gait, listing_lying, listing_thigh, listing_lumbar)

        # preprocessing  (21-54)
        (d1,d2,d3)=preprocessing(lumbar_acc)
        # d1 = {'acc': acc, 'v': v, 'ml': ml, 'ap': ap},
        # d2 = {'gyro': gyro, 'yaw': yaw, 'pitch': pitch, 'roll': roll},
        # d3 = {'magnitude': a_mag, 'fs': fs}

        # find stillness periods (55-106)
        (s_start_pt, s_end_pt, ix_stillness) = find_stillness(d3['magnitude'], d3['fs'], lying_vec_lumbar)

        # find suspected postural transitions (PT) points according to Theta (tilt angle) (152-168)
        (locs, sin_theta_pks) = find_pt_with_theta(d2['pitch'], fs)

        # Clean PT with no stillness before/after (169-186)
        locs = clean_pt(locs, ix_stillness, fs, s_start_pt, s_end_pt)

        # Postral Transition detection (234-338)
        (sit_2_stand, stand_2_sit) = pt_detection(locs, fs, d1['acc'], d2['gyro'], d2['pitch'], sin_theta_pks)

        pt = np.concatenate((sit_2_stand, stand_2_sit), axis=0)  # array of all posture transition
        # (sit to stand and stand to sit)
        pt = pt[pt[:, 0].argsort()]  # sort rows according to first column

        # Delete PT next to lying segments (334-388)
        pt = delete_PT_next_to_lying(pt, lying_vec_lumbar, ix_stillness, walking_vec_lumbar, fs)

        # Elimination1 (389-413)
        pt = elimination1(pt, ix_stillness, walking_vec_lumbar)

        # Keep sitting segements that fit standards of length & stillness (415-427)
        pt = sitting_segements_fitting_standards(walking_vec_lumbar, pt, ix_stillness, fs)

        # Elimination2 (428-437)
        pt = elimination2(pt, fs)

        # find transitions from sit to stand (439-450)
        (s2sit_index, s2stand_index) = find_sit_to_stand(sitting_vec)

        # delete still periods (452-488)
        sitting_vec = delete_still_periods(s2sit_index, walking_vec_lumbar, s2stand_index, ix_stillness,
                                           lying_vec_lumbar, fs)

        # Statistics and Performance  estimation (489-545)
        (s2sit_sensitivity, s2sit_precision, s2stand_sensitivity, s2stand_precision, sitting_acc) = \
            performance_detection(pt, s2sit_index, s2stand_index, ix_stillness, lying_vec_lumbar, sitting_vec, fs)

    return pt, s2sit_sensitivity, s2sit_precision, s2stand_sensitivity, s2stand_precision












