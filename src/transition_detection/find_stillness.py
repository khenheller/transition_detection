#find stillness periods
import pandas as pd
import numpy as np
import bottleneck as bn

def find_stillness(
    a_mag: np.ndarray,
    fs: int,
    lying_vec_lumbar: np.ndarray)-> None:
    
    """find stillness period.
    Parameters
    ----------
    a_mag: the magnitude of acceleration
    fs: sample rate
    lying_vec_lumbar:

    Returns
    -------
    s_start_pt: 
    s_end_pt:
    """

#accRSD = movstd(Amag,100);
    acc_rsd = bn.move_std(a_mag, window=100) #Moving window standard deviation along the first axis

# % gyrRSD = movstd(Gmag,100);
# % accRM = movmean(Amag-9.81,100);
    

    jerk = np.gradient(a_mag, 1/fs) #Return the gradient of an array. 1/fs --> the space betweenthe array values
    jerk_rm = np.array(pd.Series(jerk).rolling(100).mean())
    jerk_rsd = np.array(pd.Series(jerk).rolling(100).std())
    ix_stillnes = np.logical_and(jerk_rsd < 3.5, np.logical_and(acc_rsd < 0.2, np.abs(jerk_rm) < 2.5)) #define stillness

    ix_stillnes=ix_stillnes.astype(int)
    ix_stillnes2 = np.diff(ix_stillnes)
    

    if ix_stillnes[0] == 1:
        ix_stillnes2[0] = 1
    if ix_stillnes[-1] == 1:
        ix_stillnes2[-1] = -1
    

    s_start_pt = np.argwhere(ix_stillnes2==1) #the indexes where stillness starts 
    s_end_pt = np.argwhere(ix_stillnes2==-1) #the indexes where stillness ends 
    if len(s_start_pt) > len(s_end_pt):
        s_start_pt = s_start_pt[0:-2]

# Delete "spikes" of movement (> 1s) in the stillness segments


    print(f"delete_spikes - \ns_start_pt={s_start_pt}, \ns_end_pt={s_end_pt}")
    delete_spikes = np.argwhere((s_start_pt[1:-1] - s_end_pt[0:-2]) <= 2*fs)
    s_end_pt=np.delete(s_end_pt, delete_spikes[:, 0])
    s_start_pt=np.delete(s_start_pt, delete_spikes[:, 0])



    delete_short_segements = np.argwhere(s_end_pt-s_start_pt <= 2*fs)
    #s_start_pt[delete_short_segements] = []
    s_start_pt=np.delete(s_start_pt,delete_short_segements)
    s_end_pt=np.delete(s_end_pt,delete_short_segements)
    ix_stillnes = np.zeros(np.shape(ix_stillnes))


    for kk in range(len(s_start_pt)):
        np.put(ix_stillnes, [range(s_start_pt[kk], (s_end_pt[kk] + 1))], [1] * (s_end_pt[kk] - s_start_pt[kk] + 1))
    ix_lying = np.diff(lying_vec_lumbar)    



    if lying_vec_lumbar[:,1] == 1:
        ix_lying[:,1] = 1
    if lying_vec_lumbar[:,-1] == 1:
        ix_lying[:,-1] = -1


    lying_start_pt = np.argwhere(ix_lying==1)
    lying_end_pt = np.argwhere(ix_lying==-1)
    print(s_start_pt)
    print(s_end_pt)
    print(ix_stillnes)
    return(s_start_pt, s_end_pt, ix_stillnes)


