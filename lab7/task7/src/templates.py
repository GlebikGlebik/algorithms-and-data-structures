import sys
import os

from lab7.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def is_match(pattern, string):
    """
    Проверяет соответствие строки шаблону с использованием символов подстановки '?' и '*'.

    Args:
        pattern: Шаблон, который может содержать символы '?' и '*'.
        string: Строка, которую нужно проверить на соответствие шаблону.

    Returns:
        True, если строка соответствует шаблону, False в противном случае.
    """
    # Создаем мемоизацию для хранения результатов
    memo = {}

    def dp(i, j):
        # Если мы достигли конца шаблона и строки
        if i == len(pattern) and j == len(string):
            return True
        # Если мы достигли конца шаблона, но не строки
        if i == len(pattern):
            return all(x == '*' for x in pattern[i:])
        # Если мы достигли конца строки, но не шаблона
        if j == len(string):
            return all(x == '*' for x in pattern[i:])

        # Проверка мемоизации
        if (i, j) in memo:
            return memo[(i, j)]

        # Совпадение символов или символ '?'
        if pattern[i] == string[j] or pattern[i] == '?':
            memo[(i, j)] = dp(i + 1, j + 1)
        # Если символ '*' в шаблоне
        elif pattern[i] == '*':
            # '*' может соответствовать пустой строке (dp(i+1, j)) или одному символу строки (dp(i, j+1))
            memo[(i, j)] = dp(i + 1, j) or dp(i, j + 1)
        else:
            memo[(i, j)] = False

        return memo[(i, j)]

    return dp(0, 0)

def main():

    # Пример использования
    pattern = "k?t*m"
    string = "kitten"

    # Проверка соответствия
    result = 'YES' if is_match(pattern, string) else 'NO'
    print(result)  # Должен вывести "NO", так как "kitten" не соответствует шаблону "k?t*m"


if __name__ == '__main__':
    decorate(task=7, task_name='templates')
