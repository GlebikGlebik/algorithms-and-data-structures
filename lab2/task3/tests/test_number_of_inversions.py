import unittest
from lab2.task3.src.number_of_inversions import *

class TestMergeSort(unittest.TestCase):

    def test_umber_of_inversions(self):
        self.assertEqual(merge_sort_and_count([3, 2, 1], 0, len([3, 2, 1])), 3)  # 3 инверсии: (3,2), (3,1), (2,1)
        self.assertEqual(merge_sort_and_count([1, 2, 3], 0, len([1, 2, 3])), 0)  # 0 инверсий
        self.assertEqual(merge_sort_and_count([], 0, len([])), 0)  # 0 инверсий
        self.assertEqual(merge_sort_and_count([5], 0, len([5])), 0)  # 0 инверсий
        self.assertEqual(merge_sort_and_count([2, 1], 0, len([2, 1])), 1)  # 1 инверсия: (2,1)
        self.assertEqual(merge_sort_and_count([1, 2, 3, 2, 1], 0, len([1, 2, 3, 2, 1])), 4)

if __name__ == '__main__':
    unittest.main()