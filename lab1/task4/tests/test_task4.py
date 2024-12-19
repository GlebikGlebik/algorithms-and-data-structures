import unittest

from lab1.task4.src.task4 import *
from lab1.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(4)
        a = list(map(str, input_file[0].split()))
        n = str(input_file[1])
        expected_result = ['2', '0,2']

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_empty_array(self):
        # given
        n = 3
        a = [1,2,3,3,5]
        expected_result = ['2', '2,3']

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_element_found(self):
        # given
        n = 5
        a = [5]
        expected_result = ['0']  # Один элемент найден

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_element_not_found(self):
        # given
        n = 3
        a = [5]
        expected_result = ['-1']  # Один элемент, не найден

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_multiple_occurrences(self):
        # given
        n = 2
        a = [1, 2, 2, 3, 2]
        expected_result = ['3', '1,2,4']  # Несколько вхождений

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_no_occurrences(self):
        # given
        n = 4
        a = [1, 2, 3, 5]
        expected_result = ['-1']  # Элемент не найден

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_duplicates_in_array(self):
        # given
        n = 1
        a = [1, 1, 1, 1, 1]
        expected_result = ['5', '0,1,2,3,4']  # Все элементы одинаковые

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_numbers(self):
        # given
        n = 1000
        a = [999, 1000, 1001, 1002]
        expected_result = ['1']  # Найден один элемент

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_array(self):
        # given
        n = 50
        a = list(range(100))  # Массив от 0 до 99
        expected_result = ['50']  # Найден один элемент

        # when
        res = linear_search(a, n)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()