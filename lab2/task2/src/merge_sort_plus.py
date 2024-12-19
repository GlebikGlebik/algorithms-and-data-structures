import sys
import os

from lab2.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class MergeSortPlus:
    def __init__(self):
        self.indexes = []

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.merge_sort(dict(list(arr.items())[:mid]))
        right_half = self.merge_sort(dict(list(arr.items())[mid:]))

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        sorted_array = []
        i = j = 0

        l1 = min(list(left.keys()))
        r1 = max(list(right.keys()))

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

        self.indexes.append(f'{str(l1)} {str(r1)} {str(sorted_array[0][1])} {str(sorted_array[-1][1])}')
        return dict(sorted_array)


def main():
    msp = MergeSortPlus()
    input_file = read_input(2)
    arr = list(map(int, input_file[1].split()))
    inp_arr = []
    for i in range(1, len(arr)+1):
        inp_arr.append([i, arr[i-1]])
    dict_arr = dict(inp_arr)
    sorted_arr = msp.merge_sort(dict_arr)
    res = [str(x) for x in sorted_arr.values()]
    msp.indexes.append(" ".join(res))
    write_output(2, *msp.indexes)

if __name__ == '__main__':
    decorate(task = 2, task_name= 'merge_sort_plus')