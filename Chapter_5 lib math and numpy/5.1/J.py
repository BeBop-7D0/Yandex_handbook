import numpy as np


def stairs(matrix):
    dtype = matrix.dtype
    new_matrix = np.zeros((matrix.shape[0], matrix.shape[0]), dtype=dtype)
    for i in range(new_matrix.shape[0]):
        new_matrix[i] = np.roll(matrix, i)
    return new_matrix
