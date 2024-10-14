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
    for i in range(1, n, 1):
        for j in range (0, i, 1):
            if a[i] > a[i - 1]:
                if a[j] < a[i]:
                    a[j], a[i] = a[i], a[j]

end = time.perf_counter()

for q in range(n - 1):
    if a[q + 1] > a[q]:
        print("error: invalid sort")

with open ("output.txt", "w") as f:
    f.write(" ".join(a))

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()



