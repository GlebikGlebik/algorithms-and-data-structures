import unittest

from lab3.task3.src.scarecrow_sort import *
from lab3.utils import read_input


class TestScarecrowSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(3)
        n, k = list(map(int, input_file[0].split()))
        array = list(map(int, input_file[1].split()))
        expected_result = True

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_0(self):
        # given
        n, k = [3,2]
        array = [2,1,3]
        expected_result = False

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_sorted_array(self):
        # given
        n, k = [5, 2]
        array = [1, 2, 3, 4, 5]
        expected_result = True  # Массив уже отсортирован

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_reverse_sorted_array(self):
        # given
        n, k = [5, 2]
        array = [5, 4, 3, 2, 1]
        expected_result = True  # Не может быть отсортирован в соответствии с k

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_with_duplicates(self):
        # given
        n, k = [6, 3]
        array = [3, 2, 3, 1, 2, 3]
        expected_result = False  # Массив можно отсортировать

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_all_elements_equal(self):
        # given
        n, k = [4, 2]
        array = [1, 1, 1, 1]
        expected_result = True  # Все элементы одинаковые, считается отсортированным

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_negative_numbers(self):
        # given
        n, k = [5, 2]
        array = [-1, -3, -2, -4, 0]
        expected_result = False # Массив можно отсортировать

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_k(self):
        # given
        n, k = [5, 5]
        array = [5, 1, 4, 2, 3]
        expected_result = False  # Можно отсортировать, так как k >= n

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_array(self):
        # given
        n, k = [1000, 10]
        array = list(range(1000, 0, -1))  # массив от 1000 до 1
        expected_result = False  # Не может быть отсортирован в соответствии с k

        # when
        res = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(expected_result, res)
if __name__ == '__main__':
    unittest.main()