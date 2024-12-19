import sys
import os
from lab2.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def merge(L, R):
    res = []
    i, j = 0, 0
    n, m = len(L), len(R)
    while i < n and j < m:
        if L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    while j < m:
        res.append(R[j])
        j += 1
    while i < n:
        res.append(L[i])
        i += 1
    return res

def merge_sort(A):
    if len(A) <= 1:
        return A
    q = len(A) // 2
    left = merge_sort(A[:q])
    right = merge_sort(A[q:])
    return merge(left, right)

def main():
    input_file = read_input(task = 1)
    arr = list(map(int,input_file[1].split()))
    res = merge_sort(arr)
    res = [str(i) for i in res]
    write_output(1, " ".join(res))
    print(" ".join(res))

if __name__ == '__main__':
    decorate(task = 1, task_name= 'merge_sort')






