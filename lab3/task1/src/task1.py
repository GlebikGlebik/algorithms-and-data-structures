from random import *
import time
import tracemalloc

tracemalloc.start()

with open ("input.txt", "w") as f:
    n_input = input()
    array_input = input().split()
    f.write(n_input)
    f.write("\n")
    f.write(" ".join(array_input))

start = time.perf_counter()

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[randint(0, len(array) - 1)]

    left = [element for element in array if element < pivot]
    middle = [element for element in array if element == pivot]
    right = [element for element in array if element > pivot]

    return quick_sort(left) + middle + quick_sort(right)

with open("input.txt", "r") as f:
    n = int(f.readline())
    array = f.readline().split()
    array = [int(x) for x in array]
    res = quick_sort(array)

with open("output.txt", "w") as f:
    res = [str(x) for x in res]
    s = " ".join(res)
    f.write(s)

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()