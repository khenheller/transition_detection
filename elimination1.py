#elimination 1
from dbm import ndbm
import pandas as pd
import numpy as np
import bottleneck as bn
import re

def elimination1(
    pt: np.ndarray,
    ix_stillnes: np.ndarray,
    walking_vec_lumber: np.ndarray
    ):
    """find stillness period.
    Parameters
    ----------
    pt: np.ndarray
    ix_stillnes:
    walking_vec_lumber:
    
    Returns
    -------

    """    

    ind2 = [m.start() for m in re.finditer([2,2], pt[:,1].T)]
    while ind2:
        for jj in range(len(ind2)):
            val1 = ix_stillnes[range(pt[ind2[jj],0], pt(ind2[jj]+1,0))]
            stillness = val1.sum(axis = 0) / len(val1)
            val2 = walking_vec_lumber[range(pt[ind2[jj],0],pt(ind2[jj]+1,0))] 
            walking = val2.sum(axis = 0) / len(val2)
            if np.logical(stillness < 0.85, walking > 0.05):
                delete_pt = [[delete_pt], [ind2[jj]]]
            else:
                delete_pt = [[delete_pt], ind2[jj]+1]
            delete_pt = np.unique(delete_pt)
        pt[delete_pt,:] = []
        delete_pt = []
        ind2 = [m.start() for m in re.finditer([2,2], pt[:,1].T)]

    # ind2 = strfind(PT(:,2)',[2 2]);w
    # while ind2
    #     for jj = 1:length(ind2)
    #         %         if PT(ind2(jj)+1,1)-PT(ind2(jj),1) < 10*fs
    #         %             if PT(ind2(jj),6) < PT(ind2(jj)+1,1)
    #         %                 deletePT = [deletePT ; ind2(jj)];
    #         %             else
    #         %                 deletePT = [deletePT ; ind2(jj)+1];
    #         %             end
    #         %         else
    #         stillness = sum(ix_stillnes(PT(ind2(jj),1):PT(ind2(jj)+1,1))) / length(ix_stillnes(PT(ind2(jj),1):PT(ind2(jj)+1,1)));
    #         walking = sum(Walking_Vec_Lumbar(PT(ind2(jj),1):PT(ind2(jj)+1,1))) / length(Walking_Vec_Lumbar(PT(ind2(jj),1):PT(ind2(jj)+1,1)));
    #         if stillness < 0.85 | walking > 0.05
    #             deletePT = [deletePT ; ind2(jj)];
    #         else
    #             deletePT = [deletePT ; ind2(jj)+1];
    #         end
    #         %         end
    #         deletePT = unique(deletePT);
    #     end
    #     PT(deletePT,:) = [];
    #     deletePT =[];
    #     ind2 = strfind(PT(:,2)',[2 2]);
    # end    