import unittest


class TestQuickSort(unittest.TestCase):

    def test_sorted_array(self):
        array = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort(array), expected)

    def test_reverse_sorted_array(self):
        array = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort(array), expected)

    def test_random_array(self):
        array = [3, 6, 2, 8, 1, 5]
        expected = sorted(array)  # Сравниваем с встроенной сортировкой
        self.assertEqual(quick_sort(array), expected)

    def test_empty_array(self):
        array = []
        expected = []
        self.assertEqual(quick_sort(array), expected)

    def test_single_element_array(self):
        array = [42]
        expected = [42]
        self.assertEqual(quick_sort(array), expected)

    def test_array_with_duplicates(self):
        array = [3, 1, 2, 3, 3, 1]
        expected = sorted(array)  # Сравниваем с встроенной сортировкой
        self.assertEqual(quick_sort(array), expected)

if __name__ == '__main__':
    unittest.main()