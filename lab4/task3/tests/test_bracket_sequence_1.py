import unittest

class TesttestBracketSequence1(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_input(self):
        self.path = "../txtf/test_input.txt"

    def test_single_bracket(self):
        self.assertEqual(right_pos("("), "NO")
        self.assertEqual(right_pos(")"), "NO")
        self.assertEqual(right_pos("["), "NO")
        self.assertEqual(right_pos("]"), "NO")

    def test_invalid_sequences(self):
        self.assertEqual(right_pos("[)"), "NO")
        self.assertEqual(right_pos("((("), "NO")
        self.assertEqual(right_pos("([)]"), "NO")
        self.assertEqual(right_pos("{[}]"), "NO")
        self.assertEqual(right_pos("((()))"), "NO")
        self.assertEqual(right_pos("())"), "NO")
        self.assertEqual(right_pos("([)[]"), "NO")
        self.assertEqual(right_pos("[[[[]]]"), "NO")
        self.assertEqual(right_pos("]]]]"), "NO")


    def test_unbalanced_brackets(self):
        self.assertEqual(right_pos("("), "NO")
        self.assertEqual(right_pos("("), "NO")
        self.assertEqual(right_pos("("), "NO")
        self.assertEqual(right_pos("("), "NO")
        self.assertEqual(right_pos("("), "NO")

if __name__ == "__main__":
    unittest.main()