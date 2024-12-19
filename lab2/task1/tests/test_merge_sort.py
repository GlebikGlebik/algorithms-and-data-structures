import unittest

from lab2.task1.src.merge_sort import *
from lab2.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(task=1)
        arr = list(map(int, input_file[1].split()))
        expected_result = [1,2,3,4,5]

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_0(self):
        # given
        arr = [9,7,6,4,3,1,2,5,8]
        expected_result = [1,2,3,4,5,6,7,8,9]

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_empty_array(self):
        # given
        arr = []
        expected_result = []  # Пустой массив остается пустым

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_element(self):
        # given
        arr = [42]
        expected_result = [42]  # Массив из одного элемента остается без изменений

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_identical_elements(self):
        # given
        arr = [5, 5, 5, 5, 5]
        expected_result = [5, 5, 5, 5, 5]  # Все элементы одинаковые

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_negative_numbers(self):
        # given
        arr = [-3, -1, -4, -2, 0, 1, -5]
        expected_result = [-5, -4, -3, -2, -1, 0, 1]  # Сортировка отрицательных чисел

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_mixed_numbers(self):
        # given
        arr = [3, -1, 0, 2, -3, 5, 4]
        expected_result = [-3, -1, 0, 2, 3, 4, 5]  # Смешанные положительные и отрицательные числа

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_numbers(self):
        # given
        arr = [1000, 500, 2000, 1500]
        expected_result = [500, 1000, 1500, 2000]  # Большие числа

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]  # Уже отсортированный массив

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_reverse_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]  # Массив отсортирован в обратном порядке

        # when
        res = merge_sort(arr)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()