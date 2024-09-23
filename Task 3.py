import time
import sys

with open("C:\Gleb\Лабы\Алгосы\Lab-0\input.txt","w") as w:
    n = int(input())
    w.write(str(n))

start = time.perf_counter()

with open("input.txt","r") as f:
    n = f.read()
    n = int(n)
    if 0 <= n <= 10**7:
        t = True
        a = [0,1]
        for i in range (2,60,1):
            a.append((a[i - 1] + a[i - 2]) % 10)

        def calc_fib(n):
            if n <= 59:
                return a[n] % 10
            ind = n - ((n // 60) * 60)
            ind = int(ind)
            return a[ind] % 10
    else:
        t = False

end = time.perf_counter()

with open("output.txt","w") as w2:
    if t == True:
        w2.write(str(calc_fib(n)) + "\n" + "lead time: " + str(end - start) + " seconds")
    elif t == False:
        w2.write("Incorrect input, please change the data")

