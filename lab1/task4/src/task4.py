import sys
import os

from lab1.task1.src.task1 import input_file
from lab5.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def main():
    input_file = read_input(4)
    a = list(map(str, input_file[0].split()))
    n = str(input_file[1])
    k = 0
    b = []
    for i in range(len(a)):
        if a[i] == n:
            k += 1
            b.append(str(i))

    if k == 0:
        write_output(4, '-1')
    elif k == 1:
        write_output(4, b[0])
    elif k > 1:
        write_output(4, str(k))
        write_output(4, '\n')
        write_output(4, ' '.join(b))

if __name__ == '__main__':
    decorate(task = 1, task_name= 'heap')