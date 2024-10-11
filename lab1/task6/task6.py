import time

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
    for i in range(0, n, 1):
        for j in range(0, n - 1, 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


end = time.perf_counter()

with open ("output.txt", "w") as f:
    a = [str(x) for x in a]
    f.write(" ".join(a))

print(end - start)




