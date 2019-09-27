import ctmc
import unittest
import numpy as np


class Test_Errorcheck(unittest.TestCase):

    def test1(self):
        transcount = np.array([[0, 99], [99, 1]])  # error: diag <> 0
        statetime = np.array([12, 34])
        toltime = 1e-8

        with self.assertRaises(Exception) as context:
            ctmc.errorcheck(transcount, statetime, toltime)

        # print("\ntest1: " + str(context.exception))
        self.assertTrue(
            'Transition Count Matrix have diagonal'
            in str(context.exception))

    def test2(self):
        transcount = np.array([[0, 99], [99, 0]])
        statetime = np.array([12, .0])  # error: statetime for id=1 too small
        toltime = 1e-8

        with self.assertRaises(Exception) as context:
            ctmc.errorcheck(transcount, statetime, toltime)

        # print("\ntest2: " + str(context.exception))
        self.assertTrue(
            'is smaller than toltime'
            in str(context.exception))


# run
if __name__ == '__main__':
    unittest.main()
