**transition_detection** is an open source Python package that detects transitions from sitting to standing and standing to sitting from Gyroscopes and accelerometers.
The detection requires the use of 3D gyroscopes and 3D accelerometers from the lower back.
Performance of the algorithm is evaluated by recording from the subjects' thigh.


**Data Requirements:**
3 types of mat files:
1. Combination of gyroscopes and accelerometers mat files (6 X timepoints matrix) from the lower back and from the thigh.
2. Gait mat files
3. laying mat files 


**Package requirements:**
- pandas
- numpy
- Scipy
- pywt
- os
- mat73
- pyquaternion
- ahrs

**Tests requirements:**
pytest

**Papers:**
-Pham, M. H., Warmerdam, E., Elshehabi, M., Schlenstedt, C., Bergeest, L. M., Heller, M., ... & Maetzler, W. (2018). Validation of a lower back “wearable”-based sit-to-stand and stand-to-sit algorithm for patients with Parkinson's disease and older adults in a home-like environment. Frontiers in neurology, 9, 652.
-Adamowicz, L., Karahanoglu, F. I., Cicalo, C., Zhang, H., Demanuele, C., Santamaria, M., ... & Patel, S. (2020). Assessment of sit-to-stand transfers during daily life using an accelerometer on the lower back. Sensors, 20(22), 6618.



