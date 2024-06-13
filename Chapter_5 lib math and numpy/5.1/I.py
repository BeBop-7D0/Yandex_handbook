import numpy as np


def rotate(matrix, degree):
    for i in range(degree // 90):
        matrix = np.rot90(matrix, -1)
    return matrix
