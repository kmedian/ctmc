
import numpy as np


def datacheck(data, numstates, toltime):

    eligiblestates = range(numstates)

    for exid, example in enumerate(data):
        states = example[0]
        times = example[1]

        if not np.all(np.isin(states, eligiblestates)):
            raise Exception(
                ("The example id={:d} has faulty state "
                 "labels/encodings").format(exid))

        if len(np.unique(states)) < 2:
            raise Exception(
                ("The example id={:d} has only 1 distinct "
                 "state").format(exid))

        for i in range(1, len(states)):
            if states[i - 1] == states[i]:
                raise Exception(
                    ("The example id={:d} has two consequtive entries "
                     "state[{:d}]==state[{:d}]").format(exid, i - 1, i))

        for i, t in enumerate(times):
            if t < toltime:
                raise Exception(
                    ("The example id={:d} has a state[{:d}] that have not "
                     "been active for longer than toltime").format(exid, i))

    return False
