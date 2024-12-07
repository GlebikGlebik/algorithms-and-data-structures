import time
import tracemalloc

tracemalloc.start()

with open ("../txtf/input.txt", "w") as f:
    n = input()
    a = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))

start = time.perf_counter()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(dict(list(arr.items())[:mid]))
    right_half = merge_sort(dict(list(arr.items())[mid:]))

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    l1 = min(list(left.keys()))
    r1 = max(list(right.keys()))

    while i < len(left) and j < len(right):
        if list(left.values())[i] < list(right.values())[j]:
            sorted_array.append([list(left.keys())[i], list(left.values())[i]])
            i += 1
        else:
            sorted_array.append([list(right.keys())[j], list(right.values())[j]])
            j += 1

    while i < len(left):
        sorted_array.append([list(left.keys())[i], list(left.values())[i]])
        i += 1

    while j < len(right):
        sorted_array.append([list(right.keys())[j], list(right.values())[j]])
        j += 1


    f.write(str(l1) + ' ' + str(r1) + ' ' + str(sorted_array[0][1]) + ' ' + str(sorted_array[-1][1]))
    f.write("\n")
    return dict(sorted_array)

with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    arr1 = f.readline().split()
    arr = [int(x) for x in arr1]
    with open("../txtf/output.txt", "w") as f:
        inp_arr = []
        for i in range(1, len(arr)+1):
            inp_arr.append([i, arr[i-1]])
        dict_arr = dict(inp_arr)
        sorted_arr = merge_sort(dict_arr)
        res = sorted_arr.values()
        res = [str(x) for x in sorted_arr.values()]
        f.write(" ".join(res))

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()




