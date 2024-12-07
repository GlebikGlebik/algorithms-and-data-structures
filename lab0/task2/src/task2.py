import time

with open("../txtf/input.txt", "w") as w:
    n = int(input())
    w.write(str(n))

start = time.perf_counter()

with open("../txtf/input.txt", "r") as f:
    n = f.read()
    n = int(n)
    if 0 <= n <= 45:
        t = True
        def calc_fib(n):
            if n <= 1:
                return n
            a = [0, 1]
            for i in range(0, n - 1, 1):
                j = a[0] + a[1]
                a[0] = a[1]
                a[1] = j
            return a[1]
    else:
        t = False

with open("../txtf/output.txt", "w") as w2:
    if t == True:
        w2.write(str(calc_fib(n)))
    elif t == False:
        w2.write("Incorrect input, please change the data")

end = time.perf_counter()
print ("Lead Time: " + str(end - start) + " seconds")
