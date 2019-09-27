import ctmc
import unittest


class Test_Datacheck(unittest.TestCase):

    def test1(self):
        data = [
            ([0, 1], [.7, .7]),  # ok
            ([0, 1, 2], [0.5, 0.5, 0.5])  # example id=1 doesn't work
        ]
        n_states = 2  # but there are 3 states
        toltime = 1e-8

        with self.assertRaises(Exception) as context:
            ctmc.datacheck(data, n_states, toltime)

        # print("\ntest1: " + str(context.exception))
        self.assertTrue(
            'has faulty state'
            in str(context.exception))

    def test2(self):
        data = [
            ([0, 1], [.7, .7]),  # ok
            ([0], [.3])  # example id=1 doesn't work
        ]
        n_states = 2
        toltime = 1e-8

        with self.assertRaises(Exception) as context:
            ctmc.datacheck(data, n_states, toltime)

        # print("\ntest2: " + str(context.exception))
        self.assertTrue(
            'has only 1 distinct'
            in str(context.exception))

    def test3(self):
        data = [
            ([0, 1], [.7, .7]),  # ok
            ([0, 1, 1], [.3, .3, .3])  # example id=1 doesn't work
        ]
        n_states = 2
        toltime = 1e-8

        with self.assertRaises(Exception) as context:
            ctmc.datacheck(data, n_states, toltime)

        # print("\ntest3: " + str(context.exception))
        self.assertTrue(
            'has two consequtive entries'
            in str(context.exception))

    def test4(self):
        data = [
            ([0, 1], [.7, .7]),  # ok
            ([0, 1], [.3, .0])  # example id=1 doesn't work
        ]
        n_states = 2
        toltime = 1e-8

        with self.assertRaises(Exception) as context:
            ctmc.datacheck(data, n_states, toltime)

        # print("\ntest4: " + str(context.exception))
        self.assertTrue(
            'that have not been active for longer than toltime'
            in str(context.exception))

    def test5(self):
        data = [
            ([0, 1], [.7, .7]),  # ok example
        ]
        n_states = 2
        toltime = 1e-8

        flag = ctmc.datacheck(data, n_states, toltime)
        self.assertFalse(flag)


# run
if __name__ == '__main__':
    unittest.main()
