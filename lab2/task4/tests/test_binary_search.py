import unittest


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        # Создаем отсортированный словарь для тестирования
        self.sorted_dict = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

    def test_binary_search_found(self):
        # Тест на нахождение элемента
        result = binary_search(self.sorted_dict, len(self.sorted_dict), 3)
        self.assertEqual(result, 2)  # Ключ для значения 3

    def test_binary_search_not_found(self):
        # Тест на отсутствие элемента
        result = binary_search(self.sorted_dict, len(self.sorted_dict), 6)
        self.assertEqual(result, -1)  # Элемент не найден

    def test_binary_search_first_element(self):
        # Тест на нахождение первого элемента
        result = binary_search(self.sorted_dict, len(self.sorted_dict), 1)
        self.assertEqual(result, 0)  # Ключ для значения 1

    def test_binary_search_last_element(self):
        # Тест на нахождение последнего элемента
        result = binary_search(self.sorted_dict, len(self.sorted_dict), 5)
        self.assertEqual(result, 4)  # Ключ для значения 5

    def test_binary_search_empty(self):
        # Тест на пустой словарь
        empty_dict = {}
        result = binary_search(empty_dict, 0, 1)
        self.assertEqual(result, -1)  # Элемент не найден


if __name__ == '__main__':
    unittest.main()