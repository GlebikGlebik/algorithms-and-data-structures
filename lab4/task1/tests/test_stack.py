import unittest
from lab4.task1.src.stack import *
from lab4.utils import read_input


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_case_1(self):
        # given
        self.stack.input_file = read_input(1)
        expected_result = ['10', '1234'] # Пример ожидаемой высоты дерева

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        # given
        self.stack.array = ["3", "+ 10", "+ 1234", "-"]
        expected_result = ['1234']

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        # given
        self.stack.array = ["3", "+ 5", "+ 10", "-"]
        expected_result = ['10']  # Проверка на правильность извлечения последнего элемента

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        # given
        self.stack.array = ["5", "+ 100", "+ 200", "+ 300", "-", "-"]
        expected_result = ['300', '200']  # Проверка на извлечение двух последних элементов

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        # given
        self.stack.array = ["2", "+ 7", "-"]
        expected_result = ['7']  # Проверка на извлечение единственного элемента

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_6(self):
        #empty input
        # given
        self.stack.array = []
        expected_result = []  # Проверка на извлечение единственного элемента

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
