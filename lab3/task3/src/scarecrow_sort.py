import sys
import os

from lab3.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def scarecrow_sort(n, k, arr):
    groups = [[] for _ in range(k)]
    for index in range(n):
        groups[index % k].append(arr[index])

    for group in groups:
        group.sort()

    sorted_arr = sorted(arr)

    for index in range(n):
        group_index = index % k
        element_index = index // k
        if element_index >= len(groups[group_index]):
            return False
        actual_value = groups[group_index][element_index]
        expected_value = sorted_arr[index]
        if actual_value != expected_value:
            return False
    return True


def main():
    input_file = read_input(3)
    n, k = list(map(int, input_file[0].split()))
    arr = list(map(int, input_file[1].split()))
    res = scarecrow_sort(n, k, arr)

    if res:
        write_output(3, "ДА")
    else:
        write_output(3, "НЕТ")

if __name__ == '__main__':
    decorate(task = 3, task_name= 'scarecrow_sort')
