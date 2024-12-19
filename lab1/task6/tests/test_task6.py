import unittest

from lab1.task6.src.task6 import *
from lab1.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(6)
        n = int(input_file[0])
        a = list(map(int, input_file[1].split()))
        expected_result = [1,2,3,4,5]

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_empty_array(self):
        # given
        n = 9
        a = [7,9,4,6,1,3,5,2,8]
        expected_result = [1,2,3,4,5,6,7,8,9]

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_element(self):
        # given
        n = 1
        a = [5]
        expected_result = [5]  # Один элемент остается без изменений

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_sorted_array(self):
        # given
        n = 5
        a = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]  # Уже отсортированный массив

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_reverse_sorted_array(self):
        # given
        n = 5
        a = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]  # Обратный порядок

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_with_duplicates(self):
        # given
        n = 9
        a = [3, 1, 2, 3, 4, 2, 1, 5, 4]
        expected_result = [1, 1, 2, 2, 3, 3, 4, 4, 5]  # Дубликаты

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_negative_numbers(self):
        # given
        n = 5
        a = [-1, -3, -2, -5, -4]
        expected_result = [-5, -4, -3, -2, -1]  # Отрицательные числа

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_mixed_numbers(self):
        # given
        n = 6
        a = [3, -1, 0, 2, -3, 1]
        expected_result = [-3, -1, 0, 1, 2, 3]  # Смешанные числа

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_numbers(self):
        # given
        n = 5
        a = [1000, 500, 2000, 1500, 0]
        expected_result = [0, 500, 1000, 1500, 2000]  # Большие числа

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_array(self):
        # given
        n = 10
        a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Большой массив в обратном порядке

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_identical_elements(self):
        # given
        n = 5
        a = [5, 5, 5, 5, 5]
        expected_result = [5, 5, 5, 5, 5]  # Все элементы одинаковые

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_random_array(self):
        # given
        n = 20
        a = [15, 3, 8, 23, 42, 4, 16, 7, 1, 9, 18, 5, 11, 12, 6, 2, 10, 20, 14, 13]
        expected_result = sorted(a)  # Сортируем с помощью стандартной функции для проверки

        # when
        res = bubble_sort(n, a)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    decorate(task = 5, task_name= 'task5')