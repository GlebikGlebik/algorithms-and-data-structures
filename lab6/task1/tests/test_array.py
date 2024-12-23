import unittest
from lab6.task1.src.array import *

class TestCustomSet(unittest.TestCase):

    def setUp(self):
        self.custom_set = Set()

    def test_add_and_exists(self):
        # given
        x = 5
        expected_result = True

        # when
        self.custom_set.add(x)
        result = self.custom_set.exists(x)

        # then
        self.assertEqual(result, expected_result)

    def test_add_duplicate(self):
        # given
        x = 5
        self.custom_set.add(x)

        # when
        self.custom_set.add(x)  # Adding the same element again
        result = self.custom_set.exists(x)

        # then
        self.assertTrue(result)

    def test_remove_existing(self):
        # given
        x = 5
        self.custom_set.add(x)

        # when
        self.custom_set.remove(x)
        result = self.custom_set.exists(x)

        # then
        self.assertFalse(result)

    def test_remove_non_existing(self):
        # given
        x = 5

        # when
        self.custom_set.remove(x)  # Removing a non-existing element
        result = self.custom_set.exists(x)

        # then
        self.assertFalse(result)

    def test_exists_non_existing(self):
        # given
        x = 5

        # when
        result = self.custom_set.exists(x)

        # then
        self.assertFalse(result)

    def test_result_operations(self):
        # given
        operations = [
            ['A', '5'],
            ['A', '10'],
            ['?', '5'],
            ['?', '10'],
            ['D', '5'],
            ['?', '5'],
            ['?', '10']
        ]
        expected_result = ['Y', 'Y', 'N', 'Y']

        # when
        result_list = result(operations)

        # then
        self.assertEqual(result_list, expected_result)

if __name__ == '__main__':
    unittest.main()
