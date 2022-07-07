import scipy
from scipy import io
import os
import mat73
from os.path import dirname, join as pjoin
import scipy.io as sio
import pandas as pd
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

from src.transition_detection.files_lists import files_lists
from src.transition_detection.load_data import load_data
from src.transition_detection.preprocessing import preprocessing
from src.transition_detection.find_stillness import find_stillness
from src.transition_detection.find_pt_with_theta import find_pt_with_theta
from src.transition_detection.clean_pt_with_no_stillness_before_after import clean_pt
from src.transition_detection.pt_detection import from pt_detection
from src.transition_detection.delete_PT_next_to_lying import delete_PT_next_to_lying
from src.transition_detection.elimination1 import elimination1
from src.transition_detection.sitting_segements_fitting_standards import sitting_segements_fitting_standards
from src.transition_detection.find_sit_to_stand import find_sit_to_stand
from src.transition_detection.performance_detection import performance_detection


listing_acc_path= (r'C:\Users\eden\Desktop\Axivity Lumbar vs thigh\Mat files\acc')
listing_gait_path=(r'C:\Users\eden\Desktop\Axivity Lumbar vs thigh\Posture\Gait')
listing_lying_path=(r'C:\Users\eden\Desktop\Axivity Lumbar vs thigh\Posture\Lying')


(listing_acc,listing_gait,listing_lying,listing_lumbar,listing_thigh)= files_lists(listing_acc_path,listing_gait_path,listing_lying_path)

for ff in range(len(listing_lumbar)):
    (lumbar_acc, walking_vec_Lumbar, lying_vec_lumbar, thigh_acc, walking_vec_thigh, laying_vec_thigh) = load_data(ff,listing_acc_path,listing_gait_path,listing_lying_path,listing_acc,listing_gait,listing_lying,listing_thigh,listing_lumbar)

    (d1,d2,d3)=preprocessing(lumbar_acc)
    # {'acc': acc, 'v': v, 'ml': ml, 'ap': ap},
    # {'gyro': gyro, 'yaw': yaw, 'pitch': pitch, 'roll': roll},
    # {'magnitude': a_mag, 'fs': fs}

    (s_start_pt, s_end_pt, ix_stillnes)=find_stillness(d3['magnitude'], d3['fs'], lying_vec_lumbar)


    (locs, sin_theta_pks)=find_pt_with_theta(d2['pitch'], d3['fs'])

    clean_pt(locs,ix_stillnes, d3['fs'],s_start_pt,s_end_pt)


    (sit_2_stand, stand_2_sit)=pt_detection(locs, fs, acc, gyro, pitch, fuse, sin_theta_pks, draw)

    pt=delete_PT_next_to_lying(pt,lying_vec_lumbar, ix_stillnes,walking_vec_lumbar,fs=100)

    pt=elimination1(pt,ix_stillnes,walking_vec_lumber)


    pt=sitting_segements_fitting_standards(walking_vec_lumbar, pt, ix_stillnes,fs)

    #Elimination2 #428-437
    (s2sit_index, s2stand_index)=find_sit_to_stand(sitting_vec)

    # delete still periods #452-488

    (s2sit_sensitivity, s2sit_precision, s2stand_sensitivity, s2stand_precision, sitting_acc)=performance_detection(pt, s2sit_index, s2stand_index,ix_stillness, lying_vec_lumbar,sitting_vec, fs)













# for loop for every file in the main script
#load the data #1-18 #Eden

#preprocessing  #21-54 #Maayan

# find stillness periods #55-106 #shaked

#find suspected postural transitions (PT) points according to Theta (tilt angle) #152-168 #chen


#Clean PT with no stillness before/after #169-186


#Postral Transition detection #234-338
    #  fuse = imufilter #234 maybe main

#    PT = sortrows([Sit2Stand;Stand2Sit],1); #main 352

#   Delete PT next to lying segments #354-388

# Elimination1 #389-413

#  Keep sitting segements that fit standards of length & stillness #415-427

#Elimination2 #428-437

#find transitions from sit to stand #439-450

# delete still periods #452-488

# Statistics and Performance  estimation  #489-545

# Figures #546-594

