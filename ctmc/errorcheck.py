
import numpy as np


def errorcheck(transcount, statetime, toltime):
    # check transitions counting went wrong
    if np.any(np.diag(transcount) != 0):
        raise Exception(
            ("Transition Count Matrix have diagonal "
             "elements 'm[i,i] != 0'. There are no transition counts "
             "for the i-th state to itself by definition."))

    # check if statetime[i] is big enough to work as divisor
    if np.any(statetime < toltime):
        ids = ",".join([str(i) for i in np.where(statetime < toltime)[0]])
        raise Exception(
            ("The states i={:s} have each a cumulated time period"
             " that is smaller than toltime.").format(ids))

    return False
