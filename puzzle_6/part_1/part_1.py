import os
import numpy as np

def lanternfishOffspring(content):
    """ """
    if content == "":
        filepath = os.path.join(".", "puzzle_6", "input", "input.txt")
        # read input
        with open(filepath, "r") as f:
            content = f.read()
        return content
    else:
        numOfOffs = content.split(",").count("0") # count the zeros

        for i in range(9):
            if i!= 0:
                content = content.replace(str(i), str(i-1))
            else:
                content = content.replace(str(i), "7")
        content += ",8" * numOfOffs

        return content