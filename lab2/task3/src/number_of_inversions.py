import time
import tracemalloc

tracemalloc.start()

"""
with open("../txtf/input.txt", "w") as f:
    n = input()
    a = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))
"""

start = time.perf_counter()


def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = j = 0
    inversions = 0
    temp = []
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            temp.append(left_part[i])
            i += 1
        else:
            temp.append(right_part[j])
            j += 1
            inversions += len(left_part) - i

    while i < len(left_part):
        temp.append(left_part[i])
        i += 1
    while j < len(right_part):
        temp.append(right_part[j])
        j += 1
    for i, val in enumerate(temp):
        arr[left + i] = val

    return inversions


def merge_sort_and_count(arr, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2
        inversions += merge_sort_and_count(arr, left, mid)
        inversions += merge_sort_and_count(arr, mid + 1, right)
        inversions += merge_and_count(arr, left, mid, right)
    return inversions


with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

inversions = merge_sort_and_count(arr, 0, n - 1)

with open("../txtf/output.txt", "w") as f:
    f.write(str(inversions) + "\n")

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()

