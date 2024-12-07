import unittest
from lab2.task9.src.Strassens_method_for_matrix_multiplication import *


class TestMatrixOperations(unittest.TestCase):

    def test_matrix_sum(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        self.assertEqual(matrix_sum(a, b), expected)

    def test_matrix_minus(self):
        a = [[5, 6], [7, 8]]
        b = [[1, 2], [3, 4]]
        expected = [[4, 4], [4, 4]]
        self.assertEqual(matrix_minus(a, b), expected)

    def test_pad_matrix(self):
        matrix = [[1, 2], [3, 4]]
        new_size = 4
        expected = [[1, 2, 0, 0], [3, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(pad_matrix(matrix, new_size), expected)

    def test_closest_power_of_two(self):
        self.assertEqual(closest_power_of_two(5), 8)
        self.assertEqual(closest_power_of_two(8), 8)
        self.assertEqual(closest_power_of_two(15), 16)
        self.assertEqual(closest_power_of_two(1), 1)

    def test_strassen_multiplication(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]  # 1*5 + 2*7, 1*6 + 2*8; 3*5 + 4*7, 3*6 + 4*8
        result = strassen_multiplication(a, b, 2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()