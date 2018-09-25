
import scipy.sparse
import numpy as np


def aggregateevents(data, numstates):

    transcount = scipy.sparse.lil_matrix((numstates, numstates), dtype=int)
    statetime = np.zeros(numstates, dtype=float)

    for _, example in enumerate(data):
        states = example[0]
        times = example[1]

        for i, s in enumerate(states):
            statetime[s] += times[i]
            if i:
                transcount[states[i - 1], s] += 1

    return transcount.toarray(), statetime
