import sys
import os

from lab5.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


def min_heapify(array, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] < array[smallest]:
        smallest = left

    if right < n and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        swaps.append((i, smallest))
        min_heapify(array, n, smallest, swaps)

def build_min_heap(array):
    n = len(array)
    swaps = []

    # Построение пирамиды
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(array, n, i, swaps)

    return swaps

def result(swaps):
    res = [f"{len(swaps)}"]
    for swap in swaps:
        res.append(f"{swap[0]} {swap[1]}")
    return res

def main():
    input_file = read_input(4)
    array = list(map(int, input_file[1].split()))

    swaps = build_min_heap(array)
    res = result(swaps)
    write_output(4, *res)
    [print(i) for i in res]
    print()

if __name__ == "__main__":
    decorate(task=4, task_name='heap_builder')