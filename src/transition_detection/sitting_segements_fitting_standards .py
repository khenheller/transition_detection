import numpy as np
import scipy.io


def sitting_segements_fitting_standards(walking_vec_lumbar:np.ndarray,pt:np.array, ix_stillnes:np.array, fs:int):
    """ Keep sitting segements that fit standards of length & stillness
 lines: 415-427
 Parameters
 ----------
 :param pt: posture transition array
 :param ix_stillness: indices of stillness periods
 :param walking_vec_lumbar: binary vector indicating walking state according to lumbar sensor
 :param fs: sample rate

 :return:
 pt
 """


    pt2 = []

    ind1=[] #index of all the [1,2] pairs
    for i in range(len(pt[:,1])-1):
        if pt[i,1]==1:
            if pt[i+1,1]==2:
                ind1.append(i)


    for jj in range(len(ind1)):
        segment_length=pt[ind1[jj]+1,1]- pt[ind1[jj],1]
        stillness = ix_stillnes[int(pt[ind1[jj], 0]):int(pt[(ind1[jj] + 1), 0])].sum() / len(ix_stillnes[int(pt[ind1[jj], 0]):int(pt[(ind1[jj] + 1), 0])]) #sum of all the ix_stillnes values divied by the langth of the same array
        if len(walking_vec_lumbar[int(pt[ind1[jj], 0]):int(pt[(ind1[jj] + 1), 0])])!=0:
            walking = walking_vec_lumbar[int(pt[ind1[jj], 0]):int(pt[(ind1[jj] + 1), 0])].sum() / len(walking_vec_lumbar[int(pt[ind1[jj], 0]):int(pt[(ind1[jj] + 1), 0])]) #sum of all the walking_vec_lumbar values  divied by the langth of the same array
            if (stillness > 0.8) & (segment_length > 0.25*60*fs) & (walking < 0.1):
                pt2.append(pt[ind1[jj],:])
                pt2.append(pt[ind1[jj]+1,:])
    pt=pt2

    return pt
