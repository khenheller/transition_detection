# Clean PT with no stillness before/after
import pandas as pd
import numpy as np
import bottleneck as bn

def clean_pt(
    locs: np.ndarray,
    ix_stillnes:np.ndarray,
    fs: int,
    s_start_pt:None,
    s_end_pt:None
    ):
    """ Clean PT with no stillness before/after.
    Parameters
    ----------
    locs: array of the location of the transiotions

    Returns
    -------
    """
    delete_locs = []
    for ii in range(len(locs)):
        try:
            still_before_mat= ix_stillnes[range(locs[ii]-15*fs, locs[ii])]
            still_before = (still_before_mat.sum(axis=1))/(15*fs)
            still_after_mat = ix_stillnes[range(locs[ii]+1, locs[ii]+15*fs+1)]
            still_after = (still_after_mat.sum(axis=1))/(15*fs)
            if still_before < 0.5 and still_after < 0.5:
                delete_locs = [[delete_locs],[ii]]
                continue
        except:
            print("An exception occurred")    # ???????????
        c = np.intersect1d([range(locs[ii]-15*fs,locs[ii]+15*fs+1)],[[s_start_pt],[s_end_pt]])
        if not np.any(c):
            delete_locs = [[delete_locs],[ii]]
            continue
    locs[delete_locs] = []            
            
#deleteLocs = [];
#    for ii = 1:length(locs)
#        try
#            stillBefore = sum(ix_stillnes(locs(ii)-15*fs:locs(ii)-1))/(15*fs);
#            stillAfter = sum(ix_stillnes(locs(ii)+1:locs(ii)+15*fs))/(15*fs);
#            if stillBefore < 0.5 & stillAfter < 0.5p
#                deleteLocs = [deleteLocs;ii];
#                continue;
#            end
#            c = intersect((locs(ii)-15*fs:locs(ii)+15*fs),[sStartPt;sEndPt]);
#            if isempty(c)
#                deleteLocs = [deleteLocs;ii];
#                continue;
#            end
#        end
#    end
#    locs(deleteLocs) = [];    
    
