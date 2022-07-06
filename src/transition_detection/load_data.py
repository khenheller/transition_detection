import scipy
from scipy import io
import os
import mat73
from os.path import dirname, join as pjoin
import scipy.io as sio
import pandas as pd
import pandas as pd
import numpy as np



def load_data(ff:int,listingAcc_path:str,listingGait_path:str, listingLying_path:str,listingAcc:list, listingGait:list,listingLying:list,listingThigh:list,listingLumbar:list):

    idLumbar=listingLumbar[ff][0:7] #the ID of specific subject
    full_path= os.path.join(listingAcc_path,listingLumbar[ff]) #full path of lumbar ACC file of specific subject
    lumbar_ACC = mat73.loadmat(full_path) #load mat file
    lumbar_ACC=lumbar_ACC['New_Data'] #extract the lumbar ACC array


    ix = [l for l in listingGait if (idLumbar in l) & ('lumbar' in l)]
    full_path= os.path.join(listingGait_path,ix[0])
    lumbar_Gait= scipy.io.loadmat(full_path) #extract the lumbar Gait array
    walking_vec_Lumbar=lumbar_Gait['Walking_Vec']


    ix = [l for l in listingLying if (idLumbar in l) & ('lumbar' in l)]
    full_path= os.path.join(listingLying_path,ix[0])
    lumbar_Lying= scipy.io.loadmat(full_path) #extract the lumbar laying array
    lying_vec_lumbar=lumbar_Lying['Lying_Vec']

    ix = [l for l in listingThigh if idLumbar in l]
    if len(ix)>=1:
        full_path = os.path.join(listingAcc_path, ix[0])
        ACC_thigh = mat73.loadmat(full_path)
        ACC_thigh = ACC_thigh['New_Data'] #extract the thigh ACC array
    else:
        ACC_thigh=0

    ix = [l for l in listingGait if (idLumbar in l) & ('thigh' in l)]
    if len(ix)>=1: #if this data exist for specific subject
        full_path = os.path.join(listingGait_path, ix[0])
        thigh_Gait = scipy.io.loadmat(full_path)  #extract the thigh Gait array
        walking_vec_thigh=thigh_Gait['Walking_Vec']
    else:
        walking_vec_thigh=0

    ix = [l for l in listingLying if (idLumbar in l) & ('thigh' in l)]
    if len(ix)>=1:
        full_path = os.path.join(listingLying_path, ix[0])
        thigh_Lying = scipy.io.loadmat(full_path)#extract the thigh laying array
        laying_vec_thigh= thigh_Lying['Lying_Vec']
    else:
        laying_vec_thigh=0


    return lumbar_ACC, walking_vec_Lumbar, lying_vec_lumbar, ACC_thigh,walking_vec_thigh, laying_vec_thigh

