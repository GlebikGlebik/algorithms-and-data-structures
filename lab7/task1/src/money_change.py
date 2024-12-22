import sys
import os

from lab7.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def min_coins(money, coins):
    min_numbers_of_coins = [float('inf')] * (money + 1)
    min_numbers_of_coins[0] = 0  # базовый случай

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                min_numbers_of_coins[i] = min(min_numbers_of_coins[i], min_numbers_of_coins[i - coin] + 1)  # Обновляем min_numbers_of_coins

    return min_numbers_of_coins[money] if min_numbers_of_coins[money] != float('inf') else -1  # Возвращаем минимальное количество или -1


def main():
    input_file = read_input(1)
    money, k = map(int, input_file[0].split())
    coins = list(map(int, input_file[1].split()))

    min_coins_count = min_coins(money, coins)

    write_output(1, str(min_coins_count))
    print(str(min_coins_count))
    print()

if __name__ == '__main__':
    decorate(task=1, task_name='money_change')



