
# import sys
# sys.path.append('..')
import ctmc

import unittest
import numpy as np
import numpy.testing as npt


def flatten(x):
    import itertools
    return list(itertools.chain.from_iterable(
        itertools.chain.from_iterable(x)))


class Test_Datacorrection(unittest.TestCase):

    def test1(self):
        sol = [[(2, 3), (1.6, 2.7)]]

        test = [([1], [0.5]),
                ([2, 3], [1.6, 2.7])]
        res = ctmc.datacorrection(test)

        # npt.assert_allclose(res, sol)
        npt.assert_allclose(flatten(res), flatten(sol))

    def test2(self):
        sol = [[(2, 3), (1.6, 2.7)], [(4, 5, 6), (0.1, 0.2, 0.1)]]

        test = [([2, 3], [1.6, 2.7]),
                ([4, 5, 5, 6], [.1, .1, .1, .1])]
        res = ctmc.datacorrection(test)

        npt.assert_allclose(flatten(res), flatten(sol))

    def test3(self):
        sol = [[(4, 5, 6), (0.1, 0.2, 0.1)]]

        test = [([4, 5, 5, 6], [.1, .1, .1, .1]),
                ([7, 7, 7, 7], [.1, .1, .1, .1])]
        res = ctmc.datacorrection(test)

        npt.assert_allclose(flatten(res), flatten(sol))

    def test4(self):
        sol = [[(1, 2, 3), (0.1, 0.1, 0.1)], [(4, 6), (0.1, 0.1)]]

        test = [([1, 2, 3], [.1, .1, .1]),
                ([4, 5, 6], [.1, .0, .1])]
        res = ctmc.datacorrection(test)

        npt.assert_allclose(flatten(res), flatten(sol))

    def test5(self):
        sol = [[(1, 2, 3), (0.1, 0.1, 0.1)], [(4, 6), (0.1, 0.1)]]

        test = [([1, 2, 3], [.1, .1, .1]),
                ([4, 5, 6], [.1, .0, .1])]
        res = ctmc.datacorrection(test)

        npt.assert_allclose(flatten(res), flatten(sol))

    def test6(self):
        sol = [[(4, 6), (0.1, 0.1)]]

        test = [([4, 5, 6], [.1, .0, .1]),
                ([7, 8, 9], [.1, .0, .0])]
        res = ctmc.datacorrection(test)

        npt.assert_allclose(flatten(res), flatten(sol))


# run
if __name__ == '__main__':
    unittest.main()
