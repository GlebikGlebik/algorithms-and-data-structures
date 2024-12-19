import sys
import os

from lab2.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(dict(list(arr.items())[:mid]))
    right_half = merge_sort(dict(list(arr.items())[mid:]))

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if list(left.values())[i] < list(right.values())[j]:
            sorted_array.append([list(left.keys())[i], list(left.values())[i]])
            i += 1
        else:
            sorted_array.append([list(right.keys())[j], list(right.values())[j]])
            j += 1

    while i < len(left):
        sorted_array.append([list(left.keys())[i], list(left.values())[i]])
        i += 1

    while j < len(right):
        sorted_array.append([list(right.keys())[j], list(right.values())[j]])
        j += 1

    return dict(sorted_array)

def binary_search(arr_dict_sorted, n, b):
    if n == 0:
        return -1
    mid = n // 2
    if list(arr_dict_sorted.values())[mid] == b:
        return list(arr_dict_sorted.keys())[mid]
    if list(arr_dict_sorted.values())[mid] > b:
        res = binary_search(dict(list(arr_dict_sorted.items())[:mid]), len(dict(list(arr_dict_sorted.items())[:mid])), b)
    if list(arr_dict_sorted.values())[mid] < b:
        res = binary_search(dict(list(arr_dict_sorted.items())[mid + 1:]), len(dict(list(arr_dict_sorted.items())[mid + 1:])), b)
    return res

def result(arr, n, brr):
    arr_for_dict = []
    for i in range(len(arr)):
        arr_for_dict.append([i, arr[i]])
    arr_dict = dict(arr_for_dict)
    arr_dict_sorted = merge_sort(arr_dict)
    res = []
    for b in brr:
        res.append(binary_search(arr_dict_sorted, n, b))
        if res[-1] == None:
            res[-1] = -1
    return res


def main():
    input_file = read_input(4)
    n = int(input_file[0])
    arr = list(map(int, input_file[1].split()))
    m = int(input_file[2])
    brr = list(map(int,input_file[3].split()))
    res = result(arr,n,brr)
    res = [str(i) for i in res]
    write_output(4, " ".join(res))
    print(" ".join(res))

if __name__ == '__main__':
    decorate(task = 4, task_name= 'binary_search')