import os

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def sonarSweepSlidingWindow():
    """ """
    filepath = os.path.join(".", "puzzle_1", "input", "input.txt")
    try:
        v = np.loadtxt(filepath)
        vSlid = np.sum(sliding_window_view(v, window_shape=3), axis=1)
        vSlidDiff = np.ediff1d(vSlid)
        return np.count_nonzero(vSlidDiff > 0)
    except:
        raise RuntimeError(f"could not open file. check {filepath}")