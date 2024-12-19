import unittest

from lab3.task8.src.nearest_points_to_the_origin import *
from lab3.utils import read_input

class TestNearestPointsToTheOrigin(unittest.TestCase):

    def test_case_input(self):
        # given
        n, k = [2,1]
        arr_of_points = [[1,3],[-2,2]]
        expected_result = [[-2, 2]]

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

    def test_case_0(self):
        # given
        n, k = [3,2]
        arr_of_points = [[3,3],[5,-1],[-2,4]]
        expected_result = [[3,3],[-2,4]]

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

    def test_case_empty_array(self):
        # given
        n, k = [0, 0]
        arr_of_points = []
        expected_result = []  # Пустой массив, поэтому результат тоже пустой

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

    def test_case_all_points_same_distance(self):
        # given
        n, k = [4, 2]
        arr_of_points = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        expected_result = [[1, 1], [1, -1]]  # Любые две точки могут быть возвращены

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

    def test_case_negative_coordinates(self):
        # given
        n, k = [3, 1]
        arr_of_points = [[-1, -1], [-2, -2], [-3, -3]]
        expected_result = [[-1, -1]]  # Ближайшая точка

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

    def test_case_mixed_coordinates(self):
        # given
        n, k = [5, 3]
        arr_of_points = [[2, 3], [-1, -1], [4, 5], [0, 0], [-2, 2]]
        expected_result = [[0, 0], [-1, -1], [-2, 2]]  # Ближайшие точки

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_distance(self):
        # given
        n, k = [3, 2]
        arr_of_points = [[100, 100], [200, 200], [300, 300]]
        expected_result = [[100, 100], [200, 200]]  # Ближайшие точки

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

    def test_case_single_point(self):
        # given
        n, k = [1, 1]
        arr_of_points = [[1, 1]]
        expected_result = [[1, 1]]  # Единственная точка

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

    def test_case_large_array(self):
        # given
        n, k = [1000, 5]
        arr_of_points = [[i, i] for i in range(1000)]  # Точки от (0,0) до (999,999)
        expected_result = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]  # Пять ближайших точек

        # when
        res = nearest_points_to_the_origin(arr_of_points, n, k)

        # then
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()