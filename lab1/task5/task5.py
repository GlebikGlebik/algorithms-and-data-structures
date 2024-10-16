import time
import tracemalloc

tracemalloc.start()

with open ("input.txt", "w") as f:
    n = input()
    a = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))

start = time.perf_counter()

with open ("input.txt", "r") as f:
    n = int(f.readline())
    a = f.readline().split()
    a = [int(x) for x in a]
    for i in range(0, n - 1, 1):
        minimal = 10 ** 9
        for j in range (i, n, 1):
            if a[j] < minimal:
                minimal = a[j]
                min_ind = j
        a[i], a[min_ind] = a[min_ind], a[i]


end = time.perf_counter()

for q in range(n - 1):
    if a[q + 1] < a[q]:
        print("error: invalid sort")

with open ("output.txt", "w") as f:
    a = [str(x) for x in a]
    f.write(" ".join(a))

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()



