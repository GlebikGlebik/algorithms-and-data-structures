import unittest

from lab3.task9.src.nearest_points import *
from lab3.utils import read_input

class TestNearestPoints(unittest.TestCase):

    def test_case_input(self):
        # given
        n = 2
        arr_of_points = {0: (0,0), 1: (3,4)}
        expected_result = 5.0

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertEqual(expected_result, min_dist)

    def test_case_0(self):
        # given
        n = 4
        arr_of_points = {0: (7, 7), 1: (1, 100), 2: (4, 8), 3: (7, 7)}
        expected_result = 0.0

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertEqual(expected_result, min_dist)

    def test_case_negative_coordinates(self):
        # given
        n = 3
        arr_of_points = {0: (-3, -4), 1: (-1, -1), 2: (-2, -2)}
        expected_result = 1.414  # Расстояние между (-1, -1) и (-2, -2)

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertAlmostEqual(expected_result, min_dist, places=3)

    def test_case_mixed_coordinates(self):
        # given
        n = 4
        arr_of_points = {0: (2, 3), 1: (-1, -1), 2: (4, 5), 3: (0, 0)}
        expected_result = 1.414  # Расстояние между (0, 0) и (-1, -1)

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertAlmostEqual(expected_result, min_dist, places=3)

    def test_case_identical_points(self):
        # given
        n = 5
        arr_of_points = {0: (1, 1), 1: (1, 1), 2: (1, 1), 3: (1, 1), 4: (1, 1)}
        expected_result = 0.0  # Все точки идентичны

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertEqual(expected_result, min_dist)

    def test_case_large_coordinates(self):
        # given
        n = 3
        arr_of_points = {0: (1000, 1000), 1: (2000, 2000), 2: (1500, 1500)}
        expected_result = 707.1067811865476  # Расстояние между (1000, 1000) и (1500, 1500)

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertAlmostEqual(expected_result, min_dist, places=3)

    def test_case_zero_distance(self):
        # given
        n = 4
        arr_of_points = {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}
        expected_result = 0.0  # Все точки находятся в начале координат

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertEqual(expected_result, min_dist)

    def test_case_two_points(self):
        # given
        n = 2
        arr_of_points = {0: (3, 4), 1: (0, 0)}
        expected_result = 5.0  # Расстояние между (0, 0) и (3, 4)

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertEqual(expected_result, min_dist)

    def test_case_large_array(self):
        # given
        n = 1000
        arr_of_points = {i: (i, i) for i in range(1000)}  # Точки от (0,0) до (999,999)
        expected_result = 1.4142135623730951  # Расстояние между (0,0) и (1,1)

        # when
        res, min_dist = nearest_point(arr_of_points, n)

        # then
        self.assertAlmostEqual(expected_result, min_dist)

if __name__ == '__main__':
    unittest.main()