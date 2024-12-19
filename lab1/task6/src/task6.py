import sys
import os

from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def bubble_sort(n, a):
    for i in range(0, n, 1):
        for j in range(0, n - 1, 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    for q in range(n - 1):
        if a[q + 1] < a[q]:
            print("error: invalid sort")

    return a

def main():
    input_file = read_input(6)
    n = int(input_file[0])
    a = list(map(int,input_file[1].split()))
    a = bubble_sort(n, a)
    res = [str(x) for x in a]
    write_output(6, ' '.join(res))

if __name__ == '__main__':
    decorate(task = 6, task_name= 'task6')



