
from .datacheck import datacheck
from .aggregateevents import aggregateevents
from .errorcheck import errorcheck
from .generatormatrix import generatormatrix
import scipy.linalg


def ctmc(data, numstates, transintv=1.0, toltime=1e-8, debug=False):
    """ Continous Time Markov Chain

    Parameters
    ----------
    data : list of lists
        A python list of N examples (e.g. rating histories of N companies,
        the event data of N basketball games, etc.). The i-th example
        consist of one list with M_i encoded state labels and M_i the
        durations or time periods the state lasted since the recording
        started.

    numstates : int
        number of unique states

    transintv : float
        The time interval

    toltime : float
        (If debug=True) Will throw an exception if the aggregated state
        duration or aggregated time periods of any state is smaller
        than toltime.

    debug : bool
        (Default: False) If True run the ctmc.datacheck function.
        Enable this flag if you to check if your 'data' variable
        has been processed correctly.

    Returns
    -------
    transmat : ndarray
        The estimated transition/stochastic matrix.

    genmat : ndarray
        The estimated generator matrix

    transcount : ndarray

    statetime : ndarray


    Errors:
    -------
    - ctmc assumes a clean data object and does not
        autocorrect any errors as result of it

    The main error sources are

    - transitions counting (e.g. two consequtive states
        has not been aggregated, only one distinct state
        reported) and
    - a state is modeled ore required that does not occur
        in the dataset (e.g. you a certain scale in mind
        and just assume it's in the data) or resp. involved
        in any transition (e.g. an example with just one
        state)

    You can enable error checking and exceptions by setting
    debug=True. You should do this for the first run on a
    smaller dataset.

    Example:
    --------
    Use `datacheck` to check during preprocessing the
    dataset

        data = ...
        ctmc.datacheck(data, numstates, toltime)

    Disable checks in `ctmc`

        transmat, genmat, transcount, statetime = ctmc.ctmc(
            data, numstates, toltime, checks=False)

    Check aftwards if there has been an error

        ctmc.errorcheck(transcount, statetime, toltime)

    """
    # raise an exception if the data format is wrong
    if debug:
        datacheck(data, numstates, toltime)

    # aggregate event data
    transcount, statetime = aggregateevents(data, numstates)

    # raise an exception if the event data aggregation failed
    if debug:
        errorcheck(transcount, statetime, toltime)

    # create generator matrix
    genmat = generatormatrix(transcount, statetime)

    # compute matrix exponential of the generator matrix
    transmat = scipy.linalg.expm(genmat * transintv)

    # done
    return transmat, genmat, transcount, statetime
