
import numpy as np


def generatormatrix(transcount, statetime):

    tmp = transcount.copy()
    n = tmp.shape[0]

    rowsum = np.sum(tmp, axis=1)
    for i in range(n):
        tmp[i, i] = -rowsum[i]

    genmat = np.zeros(shape=(n, n), dtype=float)
    for i in range(n):
        genmat[i, :] = tmp[i, :] / statetime[i]

    return genmat
