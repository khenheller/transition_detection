# elimination2
import pandas as pd
import numpy as np
import re

def elimination2(
    pt:None,
    fs: int,
    )-> None:
    
    """
    elimination2
    Parameters
    ----------
    pt:
    fs: sample rate


    Returns
    -------

    """
    delete_pt = []
    ind1 = [m.start() for m in re.finditer([1,2], pt[:,1].T)]
    for jj in range(len(ind1)):
        segment_length = len(range(pt[ind1[jj],1], pt[ind1[jj]+1,1]))
        if segment_length < 10*fs:
            delete_pt = [[delete_pt], [ind1[jj]], [ind1[jj]+1]]
    pt[delete_pt,:] = []

    return pt

   
# deletePT = [];
# ind1 = strfind(PT(:,2)',[1 2]);
# for jj = 1:length(ind1)
#     segmentLength = length(PT(ind1(jj),1):PT(ind1(jj)+1,1));
#     if segmentLength < 10*fs
#         deletePT = [deletePT ; ind1(jj); ind1(jj)+1];
#     end
# end
# PT(deletePT,:) = [];