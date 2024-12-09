import unittest


class TestNearestPoints(unittest.TestCase):

    def test_empty_array(self):
        arr_of_points = []
        n = 0
        k = 0
        expected = []  # Нет точек
        self.assertEqual(nearest_points_to_the_origin(arr_of_points, n, k), expected)

    def test_single_point(self):
        arr_of_points = [[1, 1]]
        n = 1
        k = 1
        expected = [[1, 1]]  # Ближайшая точка
        self.assertEqual(nearest_points_to_the_origin(arr_of_points, n, k), expected)

    def test_multiple_points(self):
        arr_of_points = [[1, 2], [2, 1], [3, 3], [0, 4]]
        n = 4
        k = 2
        expected = [[1, 2], [2, 1]]  # Две ближайшие точки
        self.assertEqual(nearest_points_to_the_origin(arr_of_points, n, k), expected)

if __name__ == '__main__':
    unittest.main()