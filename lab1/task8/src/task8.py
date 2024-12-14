import sys
import os
from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def main():
    input_file = read_input(8)
    n = int(input_file[0])
    a = list(map(int, input_file[1].split()))
    res = []
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[m] > a[j]:
                m = j
        if m != i:
            p = min(m,i) + 1
            v = max(m,i) + 1
            res.append(f'Swap elements at indices {str(p)} and {str(v)}.')
        a[m], a[i] = a[i], a[m]
    write_output(8, *res, "No more swaps needed.")

    for q in range(n - 1):
        if a[q + 1] < a[q]:
            print("error: invalid sort")

if __name__ == '__main__':
    decorate(task = 8, task_name= 'task8')