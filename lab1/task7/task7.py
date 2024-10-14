from time import *
import tracemalloc

tracemalloc.start()

with open ("input.txt", "w") as f:
    n = input()
    a = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))

start = perf_counter()

def selection_sort(n, arr):
    if n == 1:
        return arr
    mn = min(arr[len(arr) - n: len(arr)])
    arr[arr.index(mn, len(arr) - n, len(arr))], arr[len(arr) - n] = arr[len(arr) - n], arr[
        arr.index(mn, len(arr) - n, len(arr))]
    if n == 2:
        return arr
    else:
        return selection_sort(n - 1, arr)

with open ("input.txt", "r") as f:
    n = int(f.readline())
    a = f.readline().split()
    a = [float(x) for x in a]
    b = a.copy()
    a = selection_sort(n, a)

end = perf_counter()

for q in range(n - 1):
    if a[q + 1] < a[q]:
        print("error: invalid sort")

with open ("output.txt", "w") as f:
    f.write(str(b.index(a[0]) + 1) + " " + str(b.index(a[n // 2]) + 1) + " " + str(b.index(a[-1]) + 1))

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()