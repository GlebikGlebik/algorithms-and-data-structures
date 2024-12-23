import unittest
from lab7.task7.src.templates import *

class TestTemplateFunction(unittest.TestCase):

    def test_exact_match(self):
        # given
        temp = "hello"
        string = "hello"
        expected_result = "YES"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)

    def test_wildcard_question_mark(self):
        # given
        temp = "he?lo"
        string = "hello"
        expected_result = "YES"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)

    def test_wildcard_star(self):
        # given
        temp = "he*lo"
        string = "hello"
        expected_result = "YES"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)

    def test_wildcard_star_multiple_characters(self):
        # given
        temp = "he*lo"
        string = "heeeeeello"
        expected_result = "YES"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)

    def test_no_match(self):
        # given
        temp = "hello"
        string = "world"
        expected_result = "NO"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)

    def test_wildcard_star_only(self):
        # given
        temp = "*"
        string = "anything"
        expected_result = "YES"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)


    def test_empty_template(self):
        # given
        temp = ""
        string = ""
        expected_result = "YES"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)

    def test_empty_string_with_star(self):
        # given
        temp = "*"
        string = ""
        expected_result = "YES"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)

    def test_empty_string_without_star(self):
        # given
        temp = "a"
        string = ""
        expected_result = "NO"

        # when
        result = template(temp, string)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()