import unittest


class TestNearestPoint(unittest.TestCase):

    def test_two_points(self):
        arr_of_points = [(0, 0), (1, 1)]
        n = 2
        expected_indexes = (0, 1)
        expected_distance = math.sqrt(2)
        result_indexes, result_distance = nearest_point(arr_of_points, n)
        self.assertEqual(result_indexes, expected_indexes)
        self.assertAlmostEqual(result_distance, expected_distance)

    def test_same_distance(self):
        arr_of_points = [(0, 0), (1, 1), (1, 0)]
        n = 3
        expected_indexes = (0, 1)  # Можно вернуть любые две точки с одинаковым расстоянием
        result_indexes, result_distance = nearest_point(arr_of_points, n)
        self.assertTrue(result_indexes in [(0, 1), (0, 2)])  # Проверяем, что результат содержит ожидаемые индексы

    def test_three_points(self):
        arr_of_points = [(0, 0), (3, 4), (6, 8)]
        n = 3
        expected_indexes = (0, 1)  # (0,0) и (3,4) ближе всего
        expected_distance = 5.0  # Расстояние между (0,0) и (3,4)
        result_indexes, result_distance = nearest_point(arr_of_points, n)
        self.assertEqual(result_indexes, expected_indexes)
        self.assertAlmostEqual(result_distance, expected_distance)

if __name__ == '__main__':
    unittest.main()