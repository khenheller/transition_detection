# Clean PT with no stillness before/after
import numpy as np


def clean_pt(
    locs: np.ndarray, ix_stillnes: np.ndarray, fs: int, s_start_pt: None, s_end_pt: None
):
    """Clean PT with no stillness before/after

    Args:
        locs (np.ndarray): locations of angle peaks.
        ix_stillnes (np.ndarray): locations stillness.
        fs (int): sampling rate.
        s_start_pt (None): stillness start.
        s_end_pt (None): stillness end.

    Returns:
        np.ndarray: locations of angle peaks.
    """
    delete_locs = []
    for ii in range(len(locs)):
        try:
            # Find all stillness before and after peak.
            still_before_mat = ix_stillnes[range(locs[ii] - 15 * fs, locs[ii])]
            still_before = (still_before_mat.sum(axis=0)) / (15 * fs)
            still_after_mat = ix_stillnes[range(locs[ii] + 1, locs[ii] + 15 * fs + 1)]
            still_after = (still_after_mat.sum(axis=0)) / (15 * fs)
            # detect short stillness periods.
            if still_before < 0.5 and still_after < 0.5:
                delete_locs = [[delete_locs], [ii]]
                continue
        except Exception as err:
            print(f"An exception occurred: {err}")
        c = np.intersect1d(
            [range(locs[ii] - 15 * fs, locs[ii] + 15 * fs + 1)],
            [[s_start_pt], [s_end_pt]],
        )
        if not np.any(c):
            delete_locs = [[delete_locs], [ii]]
            continue
    # Delete PT with no stillness before or after (or short stillness).
    locs[delete_locs] = []
    return locs
