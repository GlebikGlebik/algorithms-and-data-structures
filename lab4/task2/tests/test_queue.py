import unittest
from lab4.task2.src.queue import *
from lab4.utils import read_input


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_case_1(self):
        # given
        self.queue.input_file = read_input(2)
        expected_result = ['1', '10']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        # given
        self.queue.input_file = ['4', '+ 1', '+ 40', '+ 90', '-']
        expected_result = ['1']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        # given
        self.queue.input_file = ['5', '+ 100', '+ 200', '-', '+ 300', '-']
        expected_result = ['100', '200']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        # given
        self.queue.input_file = ['2', '+ 7', '-']
        expected_result = ['7']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        # given
        self.queue.input_file = ['3', '+ 20', '+ 30', '-']
        expected_result = ['20']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(expected_result, result)

    def test_case_6(self):
        # given
        self.queue.input_file = ['3', '+ 10', '-', '-']
        expected_result = ['10', 'None']

        # when
        result = self.queue.result()

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
