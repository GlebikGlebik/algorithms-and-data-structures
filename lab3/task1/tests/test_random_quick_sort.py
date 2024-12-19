import unittest

from lab3.task1.src.random_quick_sort import *
from lab3.utils import read_input


class TestRandomQuickSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(1)
        array =  list(map(int,input_file[1].split()))
        expected_result = [1, 2, 3, 4, 5]

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_0(self):
        # given
        array = [3, 6, 2, 8, 1, 5]
        expected_result = sorted(array)

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_1(self):
        # given
        array = []
        expected_result = []

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_2(self):
        # given
        array = [42]
        expected_result = [42]

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_3(self):
        # given
        array = [3, 1, 2, 3, 3, 1]
        expected_result = sorted(array)

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_negative_numbers(self):
        # given
        array = [-5, -1, -15, 0, 3, 2]
        expected_result = sorted(array)

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_duplicates(self):
        # given
        array = [5, 3, 5, 2, 5, 1]
        expected_result = sorted(array)

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_sorted_array(self):
        # given
        array = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_numbers(self):
        # given
        array = [1000000, 500000, 10000000, 0, -1000000]
        expected_result = sorted(array)

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_array(self):
        # given
        array = list(range(1000, 0, -1))  # массив от 1000 до 1
        expected_result = list(range(1, 1001))  # ожидаемый отсортированный массив от 1 до 1000

        # when
        res = quick_sort(array)

        # then
        self.assertEqual(expected_result, res)


if __name__ == '__main__':
    unittest.main()
