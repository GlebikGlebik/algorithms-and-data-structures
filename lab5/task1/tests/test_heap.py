import unittest

from lab5.task1.src.heap import *
from lab5.utils import read_input, write_output, decorate

class TestStringMethods(unittest.TestCase):

    def test_heap(self):
        # given
        input_file = read_input(1)
        self.arr = list(map(int, input_file[1].split()))
        self.n = int(input_file[0])
        expected_result= "NO"

        # when
        result = heap(self.arr, self.n)

        # then
        self.assertEqual(result, expected_result)

    def test_heap_2(self):
        # given
        self.arr = [1, 3, 2, 5, 4] # Example that is not a heap
        self.n = len(self.arr) - 1
        expected_result = "YES"

        # when
        result = heap(self.arr, self.n)

        # then
        self.assertEqual(result, expected_result)

    def test_is_not_heap(self):
        # given
        self.arr = [3, 1, 4, 2] # Example that is not a heap
        self.n = len(self.arr) - 1
        expected_result = "NO"

        # when
        result = heap(self.arr, self.n)

        # then
        self.assertEqual(result, expected_result)

    def test_is_heap(self):
        # given
        self.arr = [1, 3, 4, 2] # Example that is a heap
        self.n = len(self.arr) - 1
        expected_result = "YES"

        # when
        result = heap(self.arr, self.n)

        # then
        self.assertEqual(result, expected_result)

    def test_single_element(self):
        # given
        self.arr = [5]  # Single element is always a heap
        self.n = len(self.arr) - 1
        expected_result = "YES"

        # when
        result = heap(self.arr, self.n)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()