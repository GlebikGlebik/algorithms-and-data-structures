import time
from time import perf_counter

with open ("input.txt", "w") as f:
    n1 = input()
    a1 = input().split()
    f.write(n1)
    f.write("\n")
    f.write(" ".join(a1))

start = time.perf_counter()

with open ("input.txt", "r") as f:
    n = int(f.readline())
    arr = f.readline().split()
    arr = [int(x) for x in arr]

    def recursive_insertion_sort(n, arr):
        if n == 1:
            return arr

        arr = recursive_insertion_sort(n - 1, arr)
        key = arr[n - 1]
        j = n - 2

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        return arr

    a = recursive_insertion_sort(n, arr)
    a = [str(x) for x in a]

end = perf_counter()

with open ("output.txt", "w") as f:
   f.write(" ".join(a))

print(end - start)