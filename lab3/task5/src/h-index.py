from random import *
import time
import tracemalloc

tracemalloc.start()

with open ("input.txt", "w") as f:
    array_input = input().split(',')
    f.write(" ".join(array_input))

start = time.perf_counter()

def h_index(array):
    h_indexes = []
    for i in range(len(array)):
        count = 0
        for j in range(1, len(array)):
            if array[i] >= array[j]:
                count += 1
        h_indexes.append(count)
    return max(h_indexes) - 1

with open("input.txt", "r") as f:
    array = list(map(int,f.readline().split()))
    res = h_index(array)

with open("output.txt", "w") as f:
    f.write(str(res))

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()