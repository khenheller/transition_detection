import scipy
from scipy import io
import os
import mat73
from os.path import dirname, join as pjoin
import scipy.io as sio
import pandas as pd
import numpy as np
import scipy.signal
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

from src.transition_detection.files_lists import files_lists
from src.transition_detection.load_data import load_data

listingAcc_path= (r'C:\Users\eden\Desktop\Axivity Lumbar vs thigh\Mat files\acc')
listingGait_path=(r'C:\Users\eden\Desktop\Axivity Lumbar vs thigh\Posture\Gait')
listingLying_path=(r'C:\Users\eden\Desktop\Axivity Lumbar vs thigh\Posture\Lying')


(listingAcc,listingGait,listingLying,listingLumbar,listingThigh)= files_lists(listingAcc_path,listingGait_path,listingLying_path)



#for ff in range(len(listingLumbar)):
for ff in range(0,1):

    (lumbar_ACC, walking_Vec_Lumbar, lying_Vec_lumbar, ACC_thigh,walking_Vec_thigh,laying_Vec_thigh)= load_data(ff,listingAcc_path,listingGait_path, listingLying_path,listingAcc,listingGait,listingLying,listingThigh,listingLumbar)



# for loop for every file in the main script
#load the data #1-18 #Eden

#preprocessing  #21-54 #Maayan

# find stillness periods #55-106 #shaked

#find suspected postural transitions (PT) points according to Theta (tilt angle) #152-168 #chen


#Clean PT with no stillness before/after #169-186


#  fuse = imufilter #234 maybe main

#Postral Transition detection #234-338

#    PT = sortrows([Sit2Stand;Stand2Sit],1); #main 352

#   Delete PT next to lying segments #354-388

# Elimination1 #389-413

#  Keep sitting segements that fit standards of length & stillness #415-427

#Elimination2 #428-437

#find transitions from sit to stand #439-450

# delete still periods #452-488

# Statistics and Performance  estimation  #489-545

# Figures #546-594

