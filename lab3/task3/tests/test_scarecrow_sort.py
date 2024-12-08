import unittest
from lab3.task3.src.scarecrow_sort import *


class TestScarecrowSort(unittest.TestCase):

    def test_single_element_array(self):
        """Тест на массиве с одним элементом"""
        n = 1
        k = 1
        arr = [42]
        self.assertTrue(scarecrow_sort(n, k, arr))

    def test_two_elements_sorted(self):
        """Тест на массиве из двух отсортированных элементов"""
        n = 2
        k = 1
        arr = [1, 2]
        self.assertTrue(scarecrow_sort(n, k, arr))



    def test_large_array(self):
        """Тест на большом массиве с последовательными числами"""
        n = 1000
        k = 10
        arr = list(range(1, 1001))  # От 1 до 1000
        self.assertTrue(scarecrow_sort(n, k, arr))

    def test_large_array_reverse(self):
        """Тест на большом массиве в обратном порядке"""
        n = 1000
        k = 10
        arr = list(range(1000, 0, -1))  # От 1000 до 1
        self.assertFalse(scarecrow_sort(n, k, arr))

    def test_large_k_with_sorted_array(self):
        """Тест на массиве с большим k и отсортированным массивом"""
        n = 5
        k = 100
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(scarecrow_sort(n, k, arr))

    def test_large_k_with_unsorted_array(self):
        """Тест на массиве с большим k и неотсортированным массивом"""
        n = 5
        k = 100
        arr = [5, 4, 3, 2, 1]
        self.assertFalse(scarecrow_sort(n, k, arr))

    def test_k_greater_than_n(self):
        """Тест на случае, когда k значительно больше n"""
        n = 3
        k = 10
        arr = [3, 2, 1]
        self.assertFalse(scarecrow_sort(n, k, arr))


    def test_array_with_zero(self):
        """Тест на массиве, содержащем ноль"""
        n = 5
        k = 2
        arr = [0, 1, 2, 3, 4]
        self.assertTrue(scarecrow_sort(n, k, arr))




if __name__ == '__main__':
    unittest.main()