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

def merge_and_count(arr, left, mid, right):
    # Левый и правый подмассивы
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    # Индексы для итерации
    i = j = 0
    k = left
    inversions = 0

    # Временный массив для объединения
    temp = []

    # Подсчёт инверсий и слияние массивов
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            temp.append(left_part[i])
            i += 1
        else:
            temp.append(right_part[j])
            j += 1
            inversions += len(left_part) - i  # Все оставшиеся элементы в левом массиве больше текущего элемента из правого

    # Добавляем оставшиеся элементы
    while i < len(left_part):
        temp.append(left_part[i])
        i += 1
    while j < len(right_part):
        temp.append(right_part[j])
        j += 1

    # Переносим отсортированные элементы в оригинальный массив
    for i, val in enumerate(temp):
        arr[left + i] = val

    return inversions


def merge_sort_and_count(arr, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2
        # Подсчитываем инверсии в левой и правой части
        inversions += merge_sort_and_count(arr, left, mid)
        inversions += merge_sort_and_count(arr, mid + 1, right)
        # Подсчитываем инверсии между двумя частями
        inversions += merge_and_count(arr, left, mid, right)
    return inversions


with open("input.txt", "r") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

inversions = merge_sort_and_count(arr, 0, n - 1)

with open("output.txt", "w") as f:
    f.write(str(inversions) + "\n")

