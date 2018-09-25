
from sklearn.base import BaseEstimator
from .ctmc_func import ctmc
from .simulate import simulate


class Ctmc(BaseEstimator):
    """Continous Time Markov Chain, sklearn API class"""

    def __init__(self, numstates, transintv=1.0, toltime=1e-8, debug=False):
        self.numstates = numstates
        self.transintv = transintv
        self.toltime = toltime
        self.debug = debug

    def fit(self, X, y=None):
        """Calls the ctmc.ctmc function

        Parameters
        ----------
        X : list of lists
            (see ctmc function 'data')

        y
            not used, present for API consistence purpose.
        """
        self.transmat, self.genmat, self.transcount, self.statetime = ctmc(
            X, self.numstates, self.transintv, self.toltime, self.debug)
        return self

    def predict(self, X, steps=1):
        """
        Parameters
        ----------
        X : ndarray
            vector with state variables at t

        Returns
        -------
        C : ndarray
            vector with state variables at t+1
        """
        return simulate(X, self.transmat, steps)
