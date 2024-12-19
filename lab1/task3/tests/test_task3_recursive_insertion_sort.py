import unittest

from lab1.task3.src.task3_recursive_insertion_sort import *
from lab1.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(task=3)
        n = int(input_file[0])
        arr = list(map(int, input_file[1].split()))
        expected_result = [1,2,3,4,5]

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_empty_array(self):
        # given
        n = 9
        arr = [7,9,4,6,1,3,5,2,8]
        expected_result = [1,2,3,4,5,6,7,8,9]

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_element_array(self):
        # given
        n = 1
        arr = [5]
        expected_result = [5]  # Массив из одного элемента остается без изменений

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_sorted_array(self):
        # given
        n = 5
        arr = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]  # Уже отсортированный массив

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_reverse_sorted_array(self):
        # given
        n = 5
        arr = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]  # Массив в обратном порядке

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_array_with_negatives(self):
        # given
        n = 5
        arr = [3, -1, 2, 0, -5]
        expected_result = [-5, -1, 0, 2, 3]  # Массив с отрицательными числами

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_array_with_duplicates(self):
        # given
        n = 6
        arr = [3, 1, 2, 3, 1, 2]
        expected_result = [1, 1, 2, 2, 3, 3]  # Массив с дубликатами

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_numbers(self):
        # given
        n = 5
        arr = [1000, 500, 2000, 1500, 0]
        expected_result = [0, 500, 1000, 1500, 2000]  # Массив с большими числами

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_floating_point_numbers(self):
        # given
        n = 4
        arr = [1.1, 2.2, 0.5, 3.3]
        expected_result = [0.5, 1.1, 2.2, 3.3]  # Массив с числами с плавающей точкой

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_array(self):
        # given
        n = 10
        arr = [5, 3, 8, 6, 2, 7, 4, 1, 10, 9]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Большой массив

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_array_with_one_negative(self):
        # given
        n = 5
        arr = [0, 2, -1, 4, 3]
        expected_result = [-1, 0, 2, 3, 4]  # Массив с одним отрицательным числом

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

    def test_case_array_with_all_identical_elements(self):
        # given
        n = 5
        arr = [7, 7, 7, 7, 7]
        expected_result = [7, 7, 7, 7, 7]  # Все элементы одинаковые

        # when
        res = recursive_insertion_sort(n, arr)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()