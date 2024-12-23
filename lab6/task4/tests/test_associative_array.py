import unittest
from lab6.task4.src.associative_array import *

class TestAssociativeArray(unittest.TestCase):
    def setUp(self):
        self.ass_array = AssociativeArray()
        self.ass_array.ass_array = {}  # Сбросим ассоциативный массив для тестов

    def test_put_and_get(self):
        # given
        key = "key1"
        value = "value1"
        expected_result = value  # Ожидаемое значение при получении

        # when
        self.ass_array.put(key, value)
        result = self.ass_array.get(key)

        # then
        self.assertEqual(result, expected_result)

    def test_get_non_existing_key(self):
        # given
        key = "non_existing_key"

        # when
        result = self.ass_array.get(key)

        # then
        self.assertEqual(result, '<None>')

    def test_prev_existing_key(self):
        # given
        self.ass_array.put("key1", "value1")
        self.ass_array.put("key2", "value2")
        expected_result = "value1"  # Ожидаемое значение предыдущего ключа

        # when
        result = self.ass_array.prev("key2")

        # then
        self.assertEqual(result, expected_result)

    def test_prev_first_key(self):
        # given
        self.ass_array.put("key1", "value1")

        # when
        result = self.ass_array.prev("key1")

        # then
        self.assertEqual(result, "<none>")

    def test_next_existing_key(self):
        # given
        self.ass_array.put("key1", "value1")
        self.ass_array.put("key2", "value2")
        expected_result = "value2"  # Ожидаемое значение следующего ключа

        # when
        result = self.ass_array.next("key1")

        # then
        self.assertEqual(result, expected_result)

    def test_next_last_key(self):
        # given
        self.ass_array.put("key1", "value1")

        # when
        result = self.ass_array.next("key1")

        # then
        self.assertEqual(result, "<none>")

    def test_delete_existing_key(self):
        # given
        key = "key1"
        value = "value1"
        self.ass_array.put(key, value)

        # when
        self.ass_array.delete(key)
        result = self.ass_array.get(key)

        # then
        self.assertEqual(result, '<None>')

    def test_delete_non_existing_key(self):
        # given
        key = "non_existing_key"

        # when
        with self.assertRaises(KeyError):
            self.ass_array.delete(key)

if __name__ == '__main__':
    unittest.main()
