from sklearn.base import BaseEstimator
from .ctmc_func import ctmc
from .simulate import simulate
import numpy as np


class Ctmc(BaseEstimator):
    """Continous Time Markov Chain, sklearn API class"""

    def __init__(self, numstates: int = None, transintv: float = 1.0,
                 toltime: float = 1e-8, autocorrect: bool = False,
                 debug: bool = False):
        self.numstates = numstates
        self.transintv = transintv
        self.toltime = toltime
        self.autocorrect = autocorrect
        self.debug = debug

    def fit(self, X: list, y=None):
        """Calls the ctmc.ctmc function

        Parameters
        ----------
        X : list of lists
            (see ctmc function 'data')

        y
            not used, present for API consistence purpose.
        """
        self.transmat, self.genmat, self.transcount, self.statetime = ctmc(
            X, numstates=self.numstates,
            transintv=self.transintv,
            toltime=self.toltime,
            autocorrect=self.autocorrect,
            debug=self.debug)
        return self

    def predict(self, X: np.ndarray, steps: int = 1) -> np.ndarray:
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
