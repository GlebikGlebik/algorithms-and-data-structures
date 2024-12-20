import sys
import os

from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def sortland(n,a):
    b = a.copy()
    res = ''
    for i in range(1, n, 1):
        for j in range(0, i, 1):
            if a[i] < a[i - 1]:
                if a[j] > a[i]:
                    p = a[j]
                    a[j] = a[i]
                    a[i] = p

    for q in range(n - 1):
        if a[q + 1] < a[q]:
            print("error: invalid sort")

    res = f'{str(b.index(a[0]) + 1)} {str(b.index(a[n // 2]) + 1)} {str(b.index(a[-1]) + 1)}'
    return res

def main():
    input_file = read_input(7)
    n = int(input_file[0])
    a = list(map(float, input_file[1].split()))

    res = sortland(n, a)

    write_output(7, res)

if __name__ == '__main__':
    decorate(task = 7, task_name= 'task7')