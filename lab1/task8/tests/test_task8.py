import unittest

from lab1.task8.src.task8 import *
from lab1.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(8)
        n = int(input_file[0])
        a = list(map(int, input_file[1].split()))
        expected_result = ['Swap elements at indices 1 and 2.', 'Swap elements at indices 2 and 4.',
                           'Swap elements at indices 3 and 5.']

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_empty_array(self):
        # given
        n = 0
        a = []
        expected_result = []  # Пустой массив, никаких обменов не требуется

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_element(self):
        # given
        n = 1
        a = [5]
        expected_result = []  # Один элемент, никаких обменов не требуется

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_sorted_array(self):
        # given
        n = 5
        a = [1, 2, 3, 4, 5]
        expected_result = []  # Уже отсортированный массив

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_reverse_sorted_array(self):
        # given
        n = 5
        a = [5, 4, 3, 2, 1]
        expected_result = ['Swap elements at indices 1 and 5.', 'Swap elements at indices 2 and 4.']

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_negative_numbers(self):
        # given
        n = 5
        a = [-1, -3, -2, -5, -4]
        expected_result = ['Swap elements at indices 1 and 4.','Swap elements at indices 2 and 5.','Swap elements at indices 3 and 5.','Swap elements at indices 4 and 5.']

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_mixed_numbers(self):
        # given
        n = 6
        a = [3, -1, 0, 2, -3, 1]
        expected_result = ['Swap elements at indices 1 and 5.', 'Swap elements at indices 4 and 6.',
                           'Swap elements at indices 5 and 6.']

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_identical_elements(self):
        # given
        n = 5
        a = [5, 5, 5, 5, 5]
        expected_result = []  # Все элементы одинаковые

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_numbers(self):
        # given
        n = 5
        a = [1000, 500, 2000, 1500, 0]
        expected_result = ['Swap elements at indices 1 and 5.', 'Swap elements at indices 3 and 5.']

        # when
        res = swap(n, a)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()