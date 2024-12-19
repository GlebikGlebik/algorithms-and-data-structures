import unittest

from lab2.task3.src.number_of_inversions import *
from lab2.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(3)
        n = int(input_file[0])
        arr = list(map(int, input_file[1].split()))
        expected_result = '17'

        # when
        inversions = merge_sort_and_count(arr, 0, n - 1)

        # then
        self.assertEqual(expected_result, str(inversions))

    def test_case_empty_array(self):
        # given
        arr = []
        expected_result = 0  # Пустой массив не имеет инверсий

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

    def test_case_single_element(self):
        # given
        arr = [42]
        expected_result = 0  # Массив из одного элемента не имеет инверсий

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

    def test_case_identical_elements(self):
        # given
        arr = [5, 5, 5, 5, 5]
        expected_result = 0  # Все элементы одинаковые, инверсий нет

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

    def test_case_negative_numbers(self):
        # given
        arr = [-3, -1, -4, -2]
        expected_result = 3  # Отрицательные числа

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

    def test_case_mixed_numbers(self):
        # given
        arr = [3, -1, 0, 2, -3]
        expected_result = 7  # Смешанные положительные и отрицательные числа

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

    def test_case_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]
        expected_result = 0  # Уже отсортированный массив, инверсий нет

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

    def test_case_reverse_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]
        expected_result = 10  # Максимальное количество инверсий

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

    def test_case_large_numbers(self):
        # given
        arr = [1000, 500, 2000, 1500]
        expected_result = 2  # Пример с большими числами

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

    def test_case_large_inversions(self):
        # given
        arr = [1, 3, 5, 2, 4, 6]
        expected_result = 3  # Инверсии между 5 и 2, 5 и 4, 3 и 2

        # when
        inversions = merge_sort_and_count(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(expected_result, inversions)

if __name__ == '__main__':
    unittest.main()