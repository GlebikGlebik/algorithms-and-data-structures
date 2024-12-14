import sys
import os
from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def Heap(arr: int, n: int):
    for i in range(2 // 2):
        one = 2 * i
        two = 2 * i + 1

        if one <= n:
            if arr[i] > arr[one]:
                return "NO"
        if two <= n:
            if arr[i] > arr[two]:
                return "NO"
    return "YES"

def main():
    arr_input = read_input(task = 1)
    arr = arr_input[1].split()
    n = int(arr_input[0])
    res = Heap(arr, n)
    write_output(1, res)

if __name__ == '__main__':
    decorate(task = 1, task_name= 'heap')