import unittest
from lab6.task2.src.phone_book import *

class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.pb = PhoneBook()
        self.pb.phone_book = []  # Сбросим телефонную книгу для тестов

    def test_add_contact(self):
        # given
        number = "123456789"
        name = "John Doe"
        expected_result = [(number, name)]  # Ожидаемое состояние телефонной книги

        # when
        self.pb.add(number, name)

        # then
        self.assertEqual(self.pb.phone_book, expected_result)

    def test_add_duplicate_contact(self):
        # given
        number = "123456789"
        name1 = "John Doe"
        name2 = "Jane Smith"
        expected_result = [(number, name2)]  # Ожидаемое состояние телефонной книги после обновления

        # when
        self.pb.add(number, name1)
        self.pb.add(number, name2)

        # then
        self.assertEqual(self.pb.phone_book, expected_result)

    def test_delete_contact(self):
        # given
        number = "123456789"
        name = "John Doe"
        self.pb.add(number, name)
        expected_result = []  # Ожидаемое состояние телефонной книги после удаления

        # when
        self.pb.dell(number)

        # then
        self.assertEqual(self.pb.phone_book, expected_result)

    def test_find_existing_contact(self):
        # given
        number = "123456789"
        name = "John Doe"
        self.pb.add(number, name)

        # when
        result = self.pb.find(number)

        # then
        self.assertEqual(result, name)

    def test_find_non_existing_contact(self):
        # given
        number = "987654321"  # Номер, который еще не добавлен

        # when
        result = self.pb.find(number)

        # then
        self.assertEqual(result, 'not found')

if __name__ == '__main__':
    unittest.main()