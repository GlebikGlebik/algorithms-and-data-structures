import unittest
from lab4.task3.src.bracket_sequence_1 import *
from lab4.utils import read_input


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_case_input(self):
        # given
        self.stack.input_file = read_input(3)
        expected_result = ['YES', 'YES','NO','NO','NO'] # Пример ожидаемой высоты дерева

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_1(self):
        # given
        self.stack.input_file = ['1', '[]']
        expected_result = ['YES'] # Пример ожидаемой высоты дерева

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        # given
        self.stack.input_file = ['10', '[]', '[()]', '[(])', '(()', '())', '[]()', '[[]]', '((()))', '(([[]]))', '([)]']
        expected_result = ['YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO']  # Ожидаемые результаты для каждой строки

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        # given
        self.stack.input_file = ['10', '[]', '[()]', '[(])', '(()', '())', '[]()', '[[]]', '((()))', '(([[]]))', '([)]']
        expected_result = ['YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO']  # Ожидаемые результаты для каждой строки

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        # given
        self.stack.input_file = ['5', '((()))', '(()())', '(()', '()((', '[[[]]]']
        expected_result = ['YES', 'YES', 'NO', 'NO', 'YES']

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        # given
        self.stack.input_file = ['6', '([{}])', '[(])', '{[()]}', '((({}))', '([]{})', '([)]']
        expected_result = ['YES', 'NO', 'YES', 'NO', 'YES', 'NO']  # Ожидаемые результаты для каждой строки

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_6(self):
        # given
        self.stack.input_file = ['8', '[]()', '([])', '[()]', '(([]))', '((()))', '((]', '(()))', '([)]']
        expected_result = ['YES', 'YES', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO']  # Ожидаемые результаты для каждой строки

        # when
        result = self.stack.result()

        # then
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
