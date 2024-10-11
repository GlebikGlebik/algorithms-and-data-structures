import time

with open ("input.txt", "w",  encoding='utf-8') as f:
    a = input().split()
    n = input()
    f.write(" ".join(a))
    f.write("\n")
    f.write(n)

start = time.perf_counter()

with open ("input.txt", "r",  encoding='utf-8') as f:
    a = f.readline().split()
    n = f.readline()
    k = 0
    b = []
    for i in range(0, len(a), 1): #Алгоритм не может понять, что 2 одинаковых слова - одинаковы
        print (a[i])
        if a[i] == n:
            k += 1
            b.append(str(i))

end = time.perf_counter()

with open ("output.txt", "w",  encoding='utf-8') as f:
    if k == 0:
        f.write("-1")
    elif k == 1:
        f.write(str(a[0]))
    elif k > 1:
        f.write(str(k))
        f.write("\n")
        f.write(", ".join(b))

print(start - end)