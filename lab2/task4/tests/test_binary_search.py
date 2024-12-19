import unittest

from lab2.task1.src.merge_sort import *
from lab2.task4.src.binary_search import result
from lab2.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(4)
        n = int(input_file[0])
        arr = list(map(int, input_file[1].split()))
        m = int(input_file[2])
        brr = list(map(int, input_file[3].split()))

        expected_result = [2, 0, -1, 0, -1]

        # when
        res = result(arr, n, brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_empty_arrays(self):
        # given
        arr = []
        brr = []
        expected_result = []  # Пустые массивы должны вернуть пустой результат

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_brr_empty(self):
        # given
        arr = [1, 2, 3, 4, 5]
        brr = []
        expected_result = []  # Если brr пустой, то результат пустой

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_arr_empty(self):
        # given
        arr = []
        brr = [1, 2, 3]
        expected_result = [-1, -1, -1]  # Если arr пустой, то результат пустой

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_identical_elements(self):
        # given
        arr = [5, 5, 5, 5]
        brr = [5, 6, 7]
        expected_result = [1, -1, -1]  # 5 присутствует, остальные -1

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_negative_numbers(self):
        # given
        arr = [-5, -3, -1, 0, 2]
        brr = [-3, -1, 1]
        expected_result = [1, 2, -1]  # Индексы для -3, -1 и 1 не найдены

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_mixed_numbers(self):
        # given
        arr = [3, -1, 0, 2, -3]
        brr = [0, 3, -4]
        expected_result = [2, 0, -1]  # Индексы для 0, 3 и -4

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]
        brr = [1, 3, 5, 6]
        expected_result = [0, 2, 4, -1]  # Индексы для 1, 3, 5 и 6

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_reverse_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]
        brr = [1, 2, 3, 6]
        expected_result = [4, 3, 2, -1]  # Индексы для 1, 2, 3 и 6

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_numbers(self):
        # given
        arr = [1000, 500, 2000, 1500]
        brr = [1500, 1000, 2500]
        expected_result = [3, 0, -1]  # Индексы для 1500, 1000 и 2500

        # when
        res = result(arr, len(arr), brr)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    decorate(task = 4, task_name= 'binary_search')