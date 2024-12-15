import sys
import os

from lab3.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def h_index(array):
    h_indexes = []
    for i in range(len(array)):
        count = 0
        for j in range(1, len(array)):
            if array[i] >= array[j]:
                count += 1
        h_indexes.append(count)
    return max(h_indexes) - 1

def main():
    input_file = read_input(5)
    array = list(map(int,input_file[0].split(',')))
    res = h_index(array)
    write_output(5, str(res))

if __name__ == '__main__':
    decorate(task = 5, task_name= 'h_index')