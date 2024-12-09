import unittest
from lab4.task7.src.max_in_moving_sequence import *

import unittest


class TestQueue(unittest.TestCase):
    def test_queue_case_1(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("5\n1 3 5 7 9\n3\n")
        self.assertTrue('7 9 ')

    def test_queue_case_2(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("6\n10 20 30 40 50 60\n4\n")
        self.assertTrue('40 50 60 ')

    def test_queue_case_3(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("7\n5 3 8 6 2 7 4\n5\n")
        self.assertTrue('8 6 7 ')

    def test_queue_case_4(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("4\n1 2 3 4\n2\n")
        self.assertTrue('3 4 ')

    def test_queue_case_5(self):
        with open("../txtf/test_input.txt", "w") as f:
            f.write("5\n9 8 7 6 5\n1\n")
        self.assertTrue('9 ')

if __name__ == "__main__":
    unittest.main()