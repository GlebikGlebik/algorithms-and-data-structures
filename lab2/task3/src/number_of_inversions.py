import sys
import os

from lab2.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = j = 0
    inversions = 0
    temp = []
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            temp.append(left_part[i])
            i += 1
        else:
            temp.append(right_part[j])
            j += 1
            inversions += len(left_part) - i

    while i < len(left_part):
        temp.append(left_part[i])
        i += 1
    while j < len(right_part):
        temp.append(right_part[j])
        j += 1
    for i, val in enumerate(temp):
        arr[left + i] = val

    return inversions


def merge_sort_and_count(arr, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2
        inversions += merge_sort_and_count(arr, left, mid)
        inversions += merge_sort_and_count(arr, mid + 1, right)
        inversions += merge_and_count(arr, left, mid, right)
    return inversions


def main():
    input_file = read_input(3)
    n = int(input_file[0])
    arr = list(map(int, input_file[1].split()))
    inversions = merge_sort_and_count(arr, 0, n - 1)
    write_output(3, str(inversions))
    print(str(inversions))

if __name__ == '__main__':
    decorate(task = 3, task_name= 'number_of_inversions')