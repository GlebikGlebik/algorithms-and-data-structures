from time import *
import tracemalloc

tracemalloc.start()

with open ("../txtf/input.txt", "w") as f:
    n = input()
    a = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))

start = perf_counter()

with open ("../txtf/input.txt", "r") as f:
    with open ("../txtf/output.txt", "w") as g:
        n = int(f.readline())
        b = f.readline().split()
        a = [int(x) for x in b]
        for i in range(n - 1):
            m = i
            for j in range(i + 1, n):
                if a[m] > a[j]:
                    m = j
            if m != i:
                p = min(m,i) + 1
                v = max(m,i) + 1
                g.write("Swap elements at indices " + str(p) + " and " + str(v) + ".")
                g.write("\n")
            a[m], a[i] = a[i], a[m]
        g.write("No more swaps needed.")

end = perf_counter()

for q in range(n - 1):
    if a[q + 1] < a[q]:
        print("error: invalid sort")

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()