import sys
import os

from lab3.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


def h_index(array):
    array.sort(reverse=True)

    h = 0
    for i in range(len(array)):
        if array[i] >= i + 1:  # Проверяем, сколько статей имеют хотя бы i+1 цитирований
            h = i + 1
        else:
            break
    return h


def main():
    input_file = read_input(5)
    array = list(map(int, input_file[0].split(',')))
    res = h_index(array)
    write_output(5, str(res))
    print(str(res))

if __name__ == '__main__':
    decorate(task=5, task_name='h_index')