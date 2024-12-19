import unittest

from lab2.task2.src.merge_sort_plus import *
from lab2.utils import read_input

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.msp = MergeSortPlus()

    def test_case_input(self):
        # given
        dict_arr = {1: 1,2: 8,3: 2,4: 1,5:4,6:7,7:3,8:2,9:3,10:6}
        expected_result = ['1 2 1 8','4 5 1 4', '3 5 1 4', '1 5 1 8', '6 7 3 7', '9 10 3 6', '8 10 2 6', '6 10 2 7',
                           '1 10 1 8', '1 1 2 2 3 3 4 6 7 8']

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

    def test_case_empty_dict(self):
        # given
        dict_arr = {}
        expected_result = ['']  # Пустой словарь должен дать пустую строку

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

    def test_case_single_entry(self):
        # given
        dict_arr = {1: 5}
        expected_result = ['5']  # Словарь с одной записью

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

    def test_case_identical_values(self):
        # given
        dict_arr = {1: 3, 2: 3, 3: 3}
        expected_result = ['2 3 3 3', '1 3 3 3', '3 3 3']  # Все значения одинаковые

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

    def test_case_negative_numbers(self):
        # given
        dict_arr = {1: -1, 2: -3, 3: -2}
        expected_result = ['2 3 -3 -2', '1 3 -3 -1', '-3 -2 -1']  # Отрицательные числа

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

    def test_case_mixed_numbers(self):
        # given
        dict_arr = {1: 3, 2: -1, 3: 0, 4: -2}
        expected_result = ['1 2 -1 3', '3 4 -2 0', '1 4 -2 3', '-2 -1 0 3']  # Смешанные положительные и отрицательные числа

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

    def test_case_large_numbers(self):
        # given
        dict_arr = {1: 1000, 2: 500, 3: 2000, 4: 1500}
        expected_result = ['1 2 500 1000', '3 4 1500 2000', '1 4 500 2000', '500 1000 1500 2000']  # Большие числа

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

    def test_case_sorted_dict(self):
        # given
        dict_arr = {1: 1, 2: 2, 3: 3}
        expected_result = ['2 3 2 3', '1 3 1 3', '1 2 3']  # Уже отсортированный словарь

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

    def test_case_reverse_sorted_dict(self):
        # given
        dict_arr = {1: 3, 2: 2, 3: 1}
        expected_result = ['2 3 1 2', '1 3 1 3', '1 2 3']  # Словарь отсортирован в обратном порядке

        # when
        sorted_arr = self.msp.merge_sort(dict_arr)
        res = [str(x) for x in sorted_arr.values()]
        self.msp.indexes.append(" ".join(res))

        # then
        self.assertEqual(expected_result, self.msp.indexes)

if __name__ == '__main__':
    unittest.main()