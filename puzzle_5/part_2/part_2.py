import os
import numpy as np

def hidrotermalVenture():
    """ """
    filepath = os.path.join(".", "puzzle_5", "input", "input_test.txt")
    v = np.fromregex(filepath, r"\d+", dtype=[("num", np.int)])
    v = np.reshape(v["num"], (np.size(v)//2, 2))
    v = np.reshape(v, (np.size(v) // 4, 4))
    print(v)
    
    minimum = np.min(v)
    maximum = np.max(v)
    
    # dictionary
    d = {}
    for x in range(minimum, maximum+1, 1):
        for y in range(minimum, maximum+1, 1):
            d[(x, y)] = 0
    for el in v:
        if (el[0] == el[2]):
            x = el[0]
            y1 = min(el[1], el[3])
            y2 = max(el[1], el[3])
            while abs(y1-y2) > 0:
                d[(x, y1)] += 1
                y1 += 1
            d[(x, y1)] += 1
        elif (el[1] == el[3]):
            y = el[1]
            x1 = min(el[0], el[2])
            x2 = max(el[0], el[2])
            while abs(x1-x2) > 0:
                d[(x1, y)] += 1
                x1 += 1
            d[(x1, y)] += 1
        else:
            x1 = min(el[0], el[2])
            x2 = max(el[0], el[2])
            while (x1 - x2 > 0):
                if el[1] > el[3]:
                    d[(x1, )]
                    x1 += 1
    c = 0
    for key in d.keys():
        if d[key] > 1:
            c += 1
        else:
            pass
    return c
