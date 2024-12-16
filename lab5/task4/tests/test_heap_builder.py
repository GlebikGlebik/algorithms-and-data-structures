import unittest
from lab5.task4.src.heap_builder import *
from lab5.utils import read_input


class TestStack(unittest.TestCase):

    def test_case_input(self):
        # given
        array = [5, 4, 3, 2, 1]
        expected_result = ['3', '1 4', '0 1', '1 3']

        # when
        swaps = build_min_heap(array)
        res = result(swaps)

        # then
        self.assertEqual(expected_result, res)

    def test_case_0(self):
        # given
        array = [5, 4, 3, 2, 1]
        expected_result = ['3', '1 4', '0 1', '1 3']

        # when
        swaps = build_min_heap(array)
        res = result(swaps)

        # then
        self.assertEqual(expected_result, res)


    def test_case_1(self):
        # given
        array = [1, 2, 3, 4, 5]
        expected_result = ['0']  # Никаких обменов не должно быть

        # when
        swaps = build_min_heap(array)
        res = result(swaps)

        # then
        self.assertEqual(expected_result, res)

    def test_case_2(self):
        # given
        array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        expected_result = ['3', '2 6', '0 1', '1 3']

        # when
        swaps = build_min_heap(array)
        res = result(swaps)

        # then
        self.assertEqual(expected_result, res)

    def test_case_3(self):
        # given
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected_result = ['8', '4 9', '3 8', '2 6', '1 4', '4 9', '0 1', '1 3', '3 7']

        # when
        swaps = build_min_heap(array)
        res = result(swaps)

        # then
        self.assertEqual(expected_result, res)

    def test_case_4(self):
        # given
        array = [1, 3, 2, 4, 5]
        expected_result = ['0']  # Никаких обменов не должно быть

        # when
        swaps = build_min_heap(array)
        res = result(swaps)

        # then
        self.assertEqual(expected_result, res)

    def test_case_5(self):
        # given
        array = [5, 3, 8, 4, 2]
        expected_result = ['3', '1 4', '0 1', '1 4']

        # when
        swaps = build_min_heap(array)
        res = result(swaps)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()
