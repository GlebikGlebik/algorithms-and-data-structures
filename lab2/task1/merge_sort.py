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

def merge(L, R):
    res = []
    i, j = 0, 0
    n, m = len(L), len(R)
    while i < n and j < m:
        if L[i] < R[i]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    while j < m:
        res.append(R[j])
        j += 1
    while i < n:
        res.append(L[i])
        i += 1
    return res

def merge_sort(A):
    if len(A) == 1:
        return A
    q = len(A) // 2
    left = merge_sort(A[:q])
    right = merge_sort(A[q:])
    return merge(left, right)

with open("input.txt", "r") as f:
    n = int(f.readline())
    A1 = f.readline().split()
    A = [int(x) for x in A1]
    res = merge_sort(A)

with open("output.txt", "w") as f:
    res = [str(x) for x in res]
    s = " ".join(res)
    f.write(s)

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()



