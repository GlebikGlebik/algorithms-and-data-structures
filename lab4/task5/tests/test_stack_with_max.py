import unittest
from lab4.task5.src.stack_with_max import *
from lab4.utils import read_input


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_case_input(self):
        # given
        self.stack.input_file = read_input(5)
        expected_result = ['2', '2'] # Пример ожидаемой высоты дерева

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_1(self):
        # given
        self.stack.input_file = ["3", "push 1", "push 7", "pop"]
        expected_result = []

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        # given
        self.stack.input_file = ["5", "push 3", "push 5", "max", "pop", "max"]
        expected_result = ["5", "3"]  # Ожидаемые результаты для max после операций

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        # given
        self.stack.input_file = ["4", "push 1", "push 7", "pop", "max"]
        expected_result = ["1"]

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        # given
        self.stack.input_file = ["6", "push 10", "push 20", "push 5", "max", "pop", "max"]
        expected_result = ["20", "20"]  # Ожидаемые результаты для max после операций

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        # given
        self.stack.input_file = ["5", "push 15", "push 25", "push 10", "pop", "max"]
        expected_result = ["25"]  # Ожидаемое значение максимума после операций

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_6(self):
        # given
        self.stack.input_file = ["4", "push 5", "push 3", "max", "pop"]
        expected_result = ["5"]  # Ожидаемое значение максимума перед удалением

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_7(self):
        # given
        self.stack.input_file = ["7", "push 1", "push 2", "push 3", "max", "pop", "max"]
        expected_result = ["3", "2"]  # Ожидаемые результаты для max после операций

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
