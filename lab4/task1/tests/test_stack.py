import unittest
from lab4.task1.src.stack import *

import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_input(self):
        self.path = "../txtf/test_input.txt"

    def test_push_and_pop(self):
        # Проверка добавления и удаления элементов
        self.stack.push('1')
        self.assertEqual(self.stack.pop(), '1')
        self.stack.push('2')
        self.stack.push('3')
        self.assertEqual(self.stack.pop(), '3')
        self.assertEqual(self.stack.pop(), '2')

    def test_stack(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("6\n+ 1\n+ 10\n-\n+ 2\n+ 1234\n-\n")
        self.assertTrue('10\n1234\n')

    def test_stack_case_1(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("5\n+ 3\n+ 5\n-\n+ 7\n-\n")
        self.assertTrue('7\n5\n')

    def test_stack_case_2(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("4\n+ 8\n-\n+ 12\n-\n")
        self.assertTrue('12\n8\n')

    def test_stack_case_3(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("3\n+ 15\n+ 20\n-\n")
        self.assertTrue('20\n')

    def test_stack_case_4(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("7\n+ 100\n+ 200\n-\n+ 300\n-\n+ 400\n-\n")
        self.assertTrue('400\n300\n200\n')

    def test_stack_case_5(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("2\n+ 999\n-\n")
        self.assertTrue('999\n')

if __name__ == "__main__":
    unittest.main()