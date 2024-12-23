import unittest

from lab7.task1.src.money_change import *
from lab7.utils import read_input, write_output


class TestMinCoins(unittest.TestCase):
    def setUp(self):
        self.coins = [1, 3, 4]  # Пример монет
        self.money_cases = [
            (6, 2),  # 6 = 3 + 3 или 4 + 1 + 1
            (8, 3),  # 8 = 4 + 4
            (11, 4),  # 11 = 4 + 4 + 3
            (2, 1),  # 2 = 1 + 1
            (0, 0),  # 0 монет, 0 монет
            (5, 2),  # 5 = 4 + 1
            (7, 3),  # 7 = 4 + 3
            (10, 3),  # 10 = 4 + 4 + 1 + 1
        ]

    def test_min_coins_case_1(self):
        # given
        money, expected_result = self.money_cases[0]

        # when
        result = min_coins(money, self.coins)

        # then
        self.assertEqual(result, expected_result)

    def test_min_coins_case_5(self):
        # given
        money, expected_result = self.money_cases[4]

        # when
        result = min_coins(money, self.coins)

        # then
        self.assertEqual(result, expected_result)

    def test_min_coins_case_6(self):
        # given
        money, expected_result = self.money_cases[5]

        # when
        result = min_coins(money, self.coins)

        # then
        self.assertEqual(result, expected_result)


    def test_min_coins_case_8(self):
        # given
        money, expected_result = self.money_cases[7]

        # when
        result = min_coins(money, self.coins)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
