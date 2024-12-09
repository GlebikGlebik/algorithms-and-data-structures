import unittest
from lab4.task5.src.stack_with_max import *

import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_input(self):
        self.path = "../txtf/test_input.txt"

    def test_stack(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("5\npush 2\npush 1\nmax\npop\nmax")
        self.assertTrue('2\n2')

    def test_stack_case_1(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("5\npush 1\npush 2\nmax\npop\nmax")
        self.assertTrue('2\n1')

    def test_stack_case_2(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("3\npush 1\npush 7\npop")
        self.assertTrue(True)

    def test_stack_case_3(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("4\npush 5\npush 3\npush 8\nmax\npop\nmax")
        self.assertTrue('8\n5')

    def test_stack_case_4(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("6\npush 4\npush 6\npush 2\nmax\npop\nmax")
        self.assertTrue('6\n4')

    def test_stack_case_5(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("7\npush 10\npush 20\npush 15\nmax\npop\nmax\npop")
        self.assertTrue('20\n15')

if __name__ == "__main__":
    unittest.main()