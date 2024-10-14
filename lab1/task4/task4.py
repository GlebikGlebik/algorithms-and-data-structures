import time
import tracemalloc

tracemalloc.start()

with open ("input.txt", "w") as f:
    a = input().split()
    n = input()
    f.write(" ".join(a))
    f.write("\n")
    f.write(n)

start = time.perf_counter()

with open ("input.txt", "r") as f:
    a = f.readline().split()
    n = f.readline()
    k = 0
    b = []
    for i in range(0, len(a), 1):
        if a[i] == n:
            k += 1
            b.append(str(i))

end = time.perf_counter()

with open ("output.txt", "w") as f:
    if k == 0:
        f.write("-1")
    elif k == 1:
        f.write(str(a[0]))
    elif k > 1:
        f.write(str(k))
        f.write("\n")
        f.write(", ".join(b))

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()



