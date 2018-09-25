
import numpy as np


def simulate(s0, transmat, steps=1):
    """Simulate the next state

    Parameters
    ----------
    s0 : ndarray
        Vector with state variables at t=0

    transmat : ndarray
        The estimated transition/stochastic matrix.

    steps : int
        (Default: 1) The number of steps to simulate model outputs ahead.
        If steps>1 the a Mult-Step Simulation is triggered.

    Returns
    -------
    out : ndarray
        (steps=1) Vector with simulated state variables ().

        (steps>1) Matrix with out[:,step] columns (Fortran order) from a
        Multi-Step Simulation. The first column is the initial state
        vector out[:,0]=s0 for algorithmic reasons.
    """
    # Single-Step simulation
    if steps == 1:
        return np.dot(s0, transmat)

    # Multi-Step simulation
    out = np.zeros(shape=(steps + 1, len(s0)), order='C')
    out[0, :] = s0

    for i in range(1, steps + 1):
        out[i, :] = np.dot(out[i - 1, :], transmat)

    return out
