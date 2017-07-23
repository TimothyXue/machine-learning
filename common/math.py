import numpy as np

def eulerDistance(vA, vB):
    return np.sqrt(np.sum(np.power(vA-vB, 2)))