from random import *
import sys
import os

from lab3.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[randint(0, len(array) - 1)]

    left = [element for element in array if element < pivot]
    middle = [element for element in array if element == pivot]
    right = [element for element in array if element > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def main():
    input_file = read_input(1)
    array = list(map(int,input_file[1].split()))
    res = quick_sort(array)
    res = [str(x) for x in res]
    write_output(1," ".join(res))
    print(" ".join(res))

if __name__ == '__main__':
    decorate(task = 1, task_name= 'random_quick_sort')

