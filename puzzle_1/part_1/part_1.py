import os
import numpy as np

def sonarSweep():
    """ """
    filepath = os.path.join(".", "puzzle_1", "input", "input.txt")
    try:
        v = np.loadtxt(filepath)
        vDiff = np.ediff1d(v)
        return np.count_nonzero(vDiff > 0)
    except:
        raise RuntimeError(f"could not open file. check {filepath}")