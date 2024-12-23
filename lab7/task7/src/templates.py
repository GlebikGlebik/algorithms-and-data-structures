import sys
import os

from lab7.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def template(temp: str, string: str) -> str:
    n, m = len(temp), len(string)
    array = [[False] * (m + 1) for _ in range(n + 1)]
    array[0][0] = True

    for i in range(1, n + 1):
        if temp[i - 1] == '*':
            array[i][0] = array[i - 1][0]
        else:
            break

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if temp[i - 1] == string[j - 1] or temp[i - 1] == '?':
                array[i][j] = array[i - 1][j - 1]
            elif temp[i - 1] == '*':
                array[i][j] = array[i - 1][j] or array[i][j - 1]

    return "YES" if array[n][m] else "NO"

def main():
    input_file = read_input(7)
    temp = input_file[0]
    string = input_file[1]

    res = 'YES' if template(temp, string) else 'NO'
    write_output(7, res)
    print(res)
    print()

if __name__ == '__main__':
    decorate(task=7, task_name='templates')
