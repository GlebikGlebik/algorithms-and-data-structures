import time
import tracemalloc

tracemalloc.start()

"""
with open ("../txtf/input.txt", "w") as f:
    n = input()
    arr = input().split()
    m = input()
    brr = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(arr))
    f.write("\n")
    f.write(m)
    f.write("\n")
    f.write(" ".join(brr))
"""

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

with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    a1 = f.readline().split()
    arr = [int(x) for x in a1]
    m = int(f.readline())
    b1 = f.readline().split()
    brr = [int(x) for x in b1]
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
    print(res)