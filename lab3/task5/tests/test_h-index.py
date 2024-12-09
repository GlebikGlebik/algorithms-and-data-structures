import unittest
from lab3.task5.src.h_index import *

class TestHIndex(unittest.TestCase):

    def test_sorted_array(self):
        array = [1, 2, 3, 4, 5]
        expected = 3
        self.assertEqual(h_index(array), expected)

    def test_reverse_sorted_array(self):
        array = [5, 4, 3, 2, 1]
        expected = 3
        self.assertEqual(h_index(array), expected)

    def test_random_array(self):
        array = [3, 0, 6, 1, 5]
        expected = 3
        self.assertEqual(h_index(array), expected)

    def test_array_with_duplicates(self):
        array = [3, 3, 3, 3, 3]
        expected = 3
        self.assertEqual(h_index(array), expected)

if __name__ == '__main__':
    unittest.main()