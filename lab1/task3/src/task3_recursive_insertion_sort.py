import time
from time import perf_counter
import tracemalloc

tracemalloc.start()

with open ("../txtf/input.txt", "w") as f:
    n1 = input()
    a1 = input().split()
    f.write(n1)
    f.write("\n")
    f.write(" ".join(a1))

start = time.perf_counter()

with open ("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    arr = f.readline().split()
    arr = [int(x) for x in arr]

    def recursive_insertion_sort(n, arr):
        if n == 1:
            return arr

        arr = recursive_insertion_sort(n - 1, arr)
        key = arr[n - 1]
        j = n - 2

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        return arr

    a = recursive_insertion_sort(n, arr)
    for q in range(n - 1):
        if a[q + 1] < a[q]:
            print("error: invalid sort")
    a = [str(x) for x in a]

end = perf_counter()

with open ("../txtf/output.txt", "w") as f:
   f.write(" ".join(a))

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()