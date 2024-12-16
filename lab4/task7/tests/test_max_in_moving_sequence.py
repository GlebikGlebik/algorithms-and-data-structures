import unittest
from lab4.task7.src.max_in_moving_sequence import *
from lab4.utils import read_input


class TestStack(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_case_input(self):
        # given
        self.queue.input_file = read_input(7)
        expected_result = ['7', '7', '5', '6', '6']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_0(self):
        # given
        self.queue.n = 5
        self.queue.arr = [1, 3, 5, 7, 9]
        self.queue.m = 3
        expected_result = ['5', '7', '9']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_1(self):
        # given
        self.queue.n = 6
        self.queue.arr = [2, 4, 1, 3, 5, 6]
        self.queue.m = 4
        expected_result = ['4', '5', '6']  # Максимумы для каждой подгруппы

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        # given
        self.queue.n = 5
        self.queue.arr = [10, 20, 30, 40, 50]
        self.queue.m = 2
        expected_result = ['20', '30', '40', '50']  # Максимумы для каждой подгруппы

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        # given
        self.queue.n = 4
        self.queue.arr = [5, 3, 8, 1]
        self.queue.m = 3
        expected_result = ['8', '8']  # Максимумы для каждой подгруппы

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        # given
        self.queue.n = 7
        self.queue.arr = [1, 2, 3, 4, 5, 6, 7]
        self.queue.m = 5
        expected_result = ['5', '6', '7']  # Максимумы для каждой подгруппы

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        # given
        self.queue.n = 6
        self.queue.arr = [7, 3, 5, 8, 1, 2]
        self.queue.m = 4
        expected_result = ['8', '8', '8']  # Максимумы для каждой подгруппы

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_6(self):
        # given
        self.queue.n = 5
        self.queue.arr = [1, 3, 5, 7, 9]
        self.queue.m = 3
        expected_result = ['5', '7', '9']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
