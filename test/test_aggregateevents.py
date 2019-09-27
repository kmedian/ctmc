import ctmc
import unittest
import numpy as np
import numpy.testing as npt


def flatten(x):
    import itertools
    return list(itertools.chain.from_iterable(
        itertools.chain.from_iterable(x)))


class Test_Aggregateevents(unittest.TestCase):

    def test1(self):
        # test case
        data = [
            ([0, 1, 0], [0.5, 0.5, 0.5])
        ]
        n_states = 2

        # solution
        sol_mat = [[0, 1], [1, 0]]
        sol_stm = [1, .5]

        # result
        res_mat, res_stm = ctmc.aggregateevents(data, n_states)

        # compare
        npt.assert_allclose(res_mat, sol_mat)
        npt.assert_allclose(res_stm, sol_stm)


# run
if __name__ == '__main__':
    unittest.main()
