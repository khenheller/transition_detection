import re
import numpy as np

def sitting_segements_fitting_standards(pt,walking_vec_lumbar,ix_stillnes,fs):
    pt2 = []
    ind1 = [m.start() for m in re.finditer([2,1], pt[:, 1].T)]
    for jj in range(len(ind1)):
        segment_length = len(range(pt(ind1[jj],1),pt(ind1[jj]+1,1)))
        stillness = range(ix_stillnes(pt(ind1[jj],1),pt(ind1[jj]+1,1))).sum() / len(range(ix_stillnes(pt(ind1[jj],1),pt(ind1[jj]+1,1))))
        walking = range(walking_vec_lumbar(pt(ind1[jj],1),pt(ind1[jj]+1,1))).sum() / len(range((walking_vec_lumbar(pt(ind1[jj],1),pt(ind1[jj]+1,1))))
        #if (stillness > 0.8) & (segment_length > 0.25*60*fs) & (walking < 0.1):
            #pt2 = [pt2,pt(ind1[jj],:), pt(ind1[jj]+1,:)].T
    pt = pt2

    return pt




