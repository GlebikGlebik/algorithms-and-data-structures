import unittest

from lab3.task5.src.h_index import *
from lab3.utils import read_input

class TestHIndex(unittest.TestCase):

    def test_case_input(self):
        # given
        input_file = read_input(5)
        array = list(map(int, input_file[0].split(',')))
        expected_result = 3

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_0(self):
        # given
        array = [1, 3, 1]
        expected_result = 1

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_empty_array(self):
        # given
        array = []
        expected_result = 0  # H-индекс для пустого массива

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_all_zeros(self):
        # given
        array = [0, 0, 0, 0]
        expected_result = 0  # Все нули, H-индекс равен 0

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_element(self):
        # given
        array = [5]
        expected_result = 1  # Один элемент, который больше 0

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_multiple_identical_elements(self):
        # given
        array = [3, 3, 3, 3]
        expected_result = 3  # Все элементы одинаковые

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_h_index(self):
        # given
        array = [10, 8, 5, 4, 3]
        expected_result = 4  # H-индекс равен 4

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_h_index_equals_length(self):
        # given
        array = [1, 2, 3, 4, 5]
        expected_result = 3  # H-индекс равен 3, так как 3 статьи имеют 3 или более цитирований

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_descending_order(self):
        # given
        array = [6, 5, 3, 1, 0]
        expected_result = 3  # H-индекс равен 3

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_array(self):
        # given
        array = list(range(1, 1001))  # Массив от 1 до 1000
        expected_result = 500  # H-индекс равен 500

        # when
        res = h_index(array)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()