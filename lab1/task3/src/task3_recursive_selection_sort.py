import time
import tracemalloc

tracemalloc.start()

with open ("../txtf/input.txt", "w") as f:
    n = input()
    a1 = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a1))

start = time.perf_counter()

with open ("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    arr = f.readline().split()
    arr = [int(x) for x in arr]

    def insertion_sort(n, arr):
        if n == 1:
            return arr
        mn = min(arr[len(arr) - n: len(arr)])
        arr[arr.index(mn, len(arr) - n, len(arr))], arr[len(arr) - n] = arr[len(arr) - n], arr[
            arr.index(mn, len(arr) - n, len(arr))]
        if n == 2:
            return arr
        else:
            return insertion_sort(n - 1, arr)

    a = insertion_sort(n, arr)
    for q in range(n - 1):
        if a[q + 1] < a[q]:
            print("error: invalid sort")
    a = [str(x) for x in a]

end = time.perf_counter()

with open ("../txtf/output.txt", "w") as f:
   f.write(" ".join(a))

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()



