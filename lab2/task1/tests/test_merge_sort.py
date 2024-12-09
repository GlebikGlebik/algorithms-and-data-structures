import unittest
from lab2 import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([5]), [5])
        self.assertEqual(merge_sort([2, 1]), [1, 2])
        self.assertEqual(merge_sort([1, 2, 3, 2, 1]), [1, 1, 2, 2, 3])

    def test_merge_sort_2(self):
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()