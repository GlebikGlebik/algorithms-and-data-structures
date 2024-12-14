import sys
import os
from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

with open ("../txtf/input.txt", "r") as f:
    input_file = read_input(task=1)
    n = int(input_file[0])
    a = list(map(int, input_file[1].split()))

def main():
    for i in range(1, n, 1):
        for j in range (0, i, 1):
            if a[i] < a[i - 1]:
                if a[j] > a[i]:
                    p = a[j]
                    a[j] = a[i]
                    a[i] = p

    for q in range(n - 1):
        if a[q + 1] < a[q]:
            print("error: invalid sort")

    res = [str(i) for i in a]
    write_output(1, ' '.join(res))

if __name__ == '__main__':
    decorate(task=1, task_name='task1')
