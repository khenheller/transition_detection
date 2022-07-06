
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

