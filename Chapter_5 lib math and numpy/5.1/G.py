import numpy as np


def make_board(n):
    m = np.zeros((n, n), dtype='int8')
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if (i + j) % 2 == 0:
                m[i, j] = 1

    return m
