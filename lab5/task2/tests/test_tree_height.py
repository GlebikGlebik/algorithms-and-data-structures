import unittest

from lab5.task2.src.tree_height import *
from lab5.utils import read_input

class TestTreeHeightCalculator(unittest.TestCase):
    def setUp(self):
        self.tree = TreeHeightCalculator()

    def test_tree_height_case_1(self):
        # given
        input_file = read_input(2)
        self.n = int(input_file[0])
        self.parents = list(map(int, input_file[1].split()))
        expected_result = 3  # Пример ожидаемой высоты дерева

        # when
        result = self.tree.tree_height(self.n, self.parents)

        # then
        self.assertEqual(result, expected_result)

    def test_tree_height_case_2(self):
        # given
        self.n = 5
        self.parents = [-1, 0, 0, 1, 1]  # Пример дерева с высотой 3
        expected_result = 3

        # when
        result = self.tree.tree_height(self.n, self.parents)

        # then
        self.assertEqual(result, expected_result)

    def test_tree_height_case_3(self):
        # given
        self.n = 1
        self.parents = [-1]  # Дерево с одним узлом, высота 1
        expected_result = 1

        # when
        result = self.tree.tree_height(self.n, self.parents)

        # then
        self.assertEqual(result, expected_result)

    def test_tree_height_case_4(self):
        # given
        self.n = 5
        self.parents = [-1,0, 4, 0, 3]  # Пустое дерево, высота 0
        expected_result = 4

        # when
        result = self.tree.tree_height(self.n, self.parents)

        # then
        self.assertEqual(result, expected_result)

    def test_tree_height_case_5(self):
        # given
        self.n = 4
        self.parents = [-1, 0, 0, 1]  # Пример дерева с высотой 2
        expected_result = 3

        # when
        result = self.tree.tree_height(self.n, self.parents)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
