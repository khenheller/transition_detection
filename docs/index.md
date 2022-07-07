# Welcome to Transition Detection

**transition_detection** is an open source Python package that detects transitions from sitting to standing and standing to sitting from Gyroscopes and accelerometers.
The detection requires the use of 3D gyroscopes and 3D accelerometers from the lower back.
Performance of the algorithm is evaluated by recording from the subjects' thigh.

## Data Requirements
Four Files are required to run trasition detection:

1. *Lumbar Gyro and Accel* - `.mat` file with acceleromotor and gyroscope measurements taken from the subject's back. Each row is a timepoint.

| Accel X | Accel Y | Accel Z | Gyro X | Gyro Y | Gyro Z |
| --- | --- | --- | --- | --- | --- |
| xt0 | y_t0 | z_t0 | x_t0 | y_t0 | z_t0 |
| x_t1 | y_t1 | z_t1 | x_t1 | y_t1 | z_t1 |
| ... | ... | ... | ... | ... | ... |
| x_tn | y_tn | z_tn | x_tn | y_tn | z_tn |

1. *Thigh Gyro and Accel* - `.mat` file with acceleromotor and gyroscope measurements taken from the subject's thigh. Each row is a timepoint.

| Accel X | Accel Y | Accel Z | Gyro X | Gyro Y | Gyro Z |
| --- | --- | --- | --- | --- | --- |
| xt0 | y_t0 | z_t0 | x_t0 | y_t0 | z_t0 |
| x_t1 | y_t1 | z_t1 | x_t1 | y_t1 | z_t1 |
| ... | ... | ... | ... | ... | ... |
| x_tn | y_tn | z_tn | x_tn | y_tn | z_tn |

2. *Gait* - `.mat` file with a vector of 1 and 0 indicating timepoints at which the subject was walking.
2. *Laying* - `.mat` file with a vector of 1 and 0 indicating timepoints at which the subject was laying.

File name template:

1. *Lumbar Gyro and Accel* - `<7_digit_id>__*_lumbar_S<2_digit_subject_num>`
1. *Thigh Gyro and Accel* - `<7_digit_id>__*_thigh_S<2_digit_subject_num>`
1. *Gait* - `Walking_<7_digit_id>__*_lumbar_S<2_digit_subject_num>`
1. *Laying* - `LyingVec_<7_digit_id>__*_lumbar_S<2_digit_subject_num>`

## Commands

* `transition_detection(listing_acc_path, listing_gait_path, listing_lying_path)` - detect transition from files and estimate accuracy.
    * `listing_acc_path` - string, path to folder containing files: *Lumbar Gyro and Accel*, *Thigh Gyro and Accel*
    * `listing_gait_path` - string, path to folder containing files: *Gait*
    * `listing_lying_path` - string, path to folder containing files: *Laying*

## Package requirements
- pandas
- numpy
- Scipy
- pywt
- os
- mat73
- pyquaternion
- ahrs

## Tests requirements
- pytest

## References
- Pham, M. H., Warmerdam, E., Elshehabi, M., Schlenstedt, C., Bergeest, L. M., Heller, M., ... & Maetzler, W. (2018). Validation of a lower back “wearable”-based sit-to-stand and stand-to-sit algorithm for patients with Parkinson's disease and older adults in a home-like environment. *Frontiers in neurology*, 9, 652.
- Adamowicz, L., Karahanoglu, F. I., Cicalo, C., Zhang, H., Demanuele, C., Santamaria, M., ... & Patel, S. (2020). Assessment of sit-to-stand transfers during daily life using an accelerometer on the lower back. Sensors, 20(22), 6618.