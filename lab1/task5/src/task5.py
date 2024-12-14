import sys
import os

from lab1.task1.src.task1 import input_file
from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def main():
    input_file = read_input(5)
    n = int(input_file[0])
    a = list(map(int, input_file[1].split()))
    for i in range(0, n - 1, 1):
        minimal = 10 ** 9
        for j in range (i, n, 1):
            if a[j] < minimal:
                minimal = a[j]
                min_ind = j
        a[i], a[min_ind] = a[min_ind], a[i]


    for q in range(n - 1):
        if a[q + 1] < a[q]:
            print("error: invalid sort")

    res = [str(x) for x in a]
    write_output(5, ' '.join(res))

if __name__ == '__main__':
    decorate(task = 5, task_name= 'task5')

