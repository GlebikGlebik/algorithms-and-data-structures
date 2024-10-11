import time
with open ("input.txt", "w") as f:
    n = input()
    a1 = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a1))

start = time.perf_counter()

with open ("input.txt", "r") as f:
    n = int(f.readline())
    arr = f.readline().split()
    arr = [int(x) for x in arr]

    def insertion_sort(n, arr):
        if n == 1:
            return arr
        mn = min(arr[len(arr) - n: len(arr)])
        arr[arr.index(mn, len(arr) - n, len(arr))], arr[len(arr) - n] = arr[len(arr) - n], arr[
            arr.index(mn, len(arr) - n, len(arr))]
        if n == 2:
            return arr
        else:
            return insertion_sort(n - 1, arr)

    a = insertion_sort(n, arr)
    a = [str(x) for x in a]

end = time.perf_counter()

with open ("output.txt", "w") as f:
   f.write(" ".join(a))

print(end - start)




