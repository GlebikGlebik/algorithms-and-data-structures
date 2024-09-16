import time

with open("input.txt","w") as w:
    n = input()
    w.write(n)

start = time.perf_counter()

with open("input.txt","r") as f:
    n = f.read()
    n = int(n)
    def calc_fib(n):
        if n <= 1:
            return n
        a = [0, 1]
        for i in range(0, n - 1, 1):
            j = a[0] + a[1]
            a[0] = a[1]
            a[1] = j
        return a[1]

with open("output.txt","w") as w2:
    w2.write(str(calc_fib(n)))

end = time.perf_counter()
print ("Lead Time: " + str(end - start) + " seconds")
