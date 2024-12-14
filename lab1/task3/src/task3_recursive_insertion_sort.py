import sys
import os

from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def recursive_insertion_sort(n, arr):
    if n == 1:
        return arr

    arr = recursive_insertion_sort(n - 1, arr)
    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
    return arr

def main():
    input_file = read_input(task=3)
    n = int(input_file[0])
    arr = list(map(int, input_file[1].split()))
    res = recursive_insertion_sort(n, arr)

    for q in range(n - 1):
        if res[q + 1] < res[q]:
            print("error: invalid sort")

    res = [str(x) for x in res]
    write_output(3, ' '.join(res))

if __name__ == '__main__':
    decorate(task = 3, task_name= 'task3_recursive_insertion_sort')