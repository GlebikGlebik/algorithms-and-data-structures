import unittest

from lab2.task9.src.Strassens_method_for_matrix_multiplication import *
from lab2.utils import read_input

class TestMergeSort(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(9)
        n = int(input_file[0])

        expected_result = ['30 24 18', '84 69 54', '138 114 90']

        # when
        res = result(input_file, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_zero_matrix(self):
        # given
        input_file = [
            '2',  # размер матрицы
            '0 0',  # первая матрица
            '0 0'   # вторая матрица
        ]
        n = int(input_file[0])

        expected_result = ['0 0', '0 0']  # Результат должен быть нулевая матрица

        # when
        res = result(input_file, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_identity_matrix(self):
        # given
        input_file = [
            '2',  # размер матрицы
            '1 0',  # первая матрица (единичная)
            '0 1'   # вторая матрица (единичная)
        ]
        n = int(input_file[0])

        expected_result = ['0 1', '0 0']  # Результат должен быть единичная матрица

        # when
        res = result(input_file, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_negative_numbers(self):
        # given
        input_file = [
            '2',  # размер матрицы
            '-1 -2',  # первая матрица
            '-3 -4'   # вторая матрица
        ]
        n = int(input_file[0])

        expected_result = ['3 4', '0 0']  # Результат произведения

        # when
        res = result(input_file, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_numbers(self):
        # given
        input_file = [
            '2',  # размер матрицы
            '1000 2000',  # первая матрица
            '3000 4000'   # вторая матрица
        ]
        n = int(input_file[0])

        expected_result = ['3000000 4000000', '0 0']  # Результат произведения

        # when
        res = result(input_file, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_element_matrices(self):
        # given
        input_file = [
            '1',  # размер матрицы
            '5',  # первая матрица
            '10'   # вторая матрица
        ]
        n = int(input_file[0])

        expected_result = ['50']  # Результат произведения

        # when
        res = result(input_file, n)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_matrix(self):
        # given
        input_file = [
            '3',  # размер матрицы
            '1 2 3',  # первая матрица
            '4 5 6',  # вторая матрица
            '7 8 9'   # третья матрица
        ]
        n = 3

        expected_result = ['4 5 6', '0 0 0', '0 0 0']  # Ожидаемый результат

        # when
        res = result(input_file, n)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()