import unittest

from lab1.task7.src.task7 import *
from lab1.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(7)
        n = int(input_file[0])
        a = list(map(float, input_file[1].split()))
        expected_result = '3 4 1'

        # when
        b = sortland(n, a)

        # then
        self.assertEqual(expected_result, b)

    def test_case_single_element(self):
        # given
        n = 1
        a = [5.0]
        expected_result = '1 1 1'  # Один элемент

        # when
        b = sortland(n, a)

        # then
        self.assertEqual(expected_result, b)

    def test_case_sorted_array(self):
        # given
        n = 5
        a = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_result = '1 3 5'  # Первый, средний и последний индексы

        # when
        b = sortland(n, a)

        # then
        self.assertEqual(expected_result, b)

    def test_case_reverse_sorted_array(self):
        # given
        n = 5
        a = [5.0, 4.0, 3.0, 2.0, 1.0]
        expected_result = '5 3 1'  # Первый, средний и последний индексы

        # when
        b = sortland(n, a)

        # then
        self.assertEqual(expected_result, b)

    def test_case_with_duplicates(self):
        # given
        n = 9
        a = [3.0, 1.0, 2.0, 3.0, 4.0, 2.0, 1.0, 5.0, 4.0]
        expected_result = '2 1 8'  # Индексы первого, среднего и последнего элементов

        # when
        b = sortland(n, a)

        # then
        self.assertEqual(expected_result, b)


    def test_case_large_numbers(self):
        # given
        n = 5
        a = [1000.0, 500.0, 2000.0, 1500.0, 0.0]
        expected_result = '5 1 3'  # Индексы первого, среднего и последнего элементов

        # when
        b = sortland(n, a)

        # then
        self.assertEqual(expected_result, b)

if __name__ == '__main__':
    decorate(task = 7, task_name= 'task7')