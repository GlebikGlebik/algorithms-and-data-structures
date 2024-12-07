# Задача 3: Сортировка вставками по убыванию

## Описание

В данной задаче реализуется алгоритм сортировки вставками по убыванию. Алгоритм проходит по элементам массива и вставляет каждый элемент в его правильную позицию среди уже отсортированных элементов, упорядочивая их по убыванию.

### Формат входных данных
- Входные данные находятся в файле `input.txt`.
- Первая строка содержит одно число `n` (1 ≤ n ≤ 1000) — количество элементов в массиве.
- Вторая строка содержит `n` целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле `output.txt` должен содержаться отсортированный массив по убыванию. Все числа должны быть разделены ровно одним пробелом.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Код задачи

```python
import time
from time import perf_counter
import tracemalloc

tracemalloc.start()

with open ("../txtf/input.txt", "w") as f:
    n1 = input()
    a1 = input().split()
    f.write(n1)
    f.write("\n")
    f.write(" ".join(a1))

start = time.perf_counter()

with open ("../txtf/input.txt", "r") as f:
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
    for q in range(n - 1):
        if a[q + 1] < a[q]:
            print("error: invalid sort")
    a = [str(x) for x in a]

end = perf_counter()

with open ("../txtf/output.txt", "w") as f:
   f.write(" ".join(a))

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()
```

## Запуск проекта

1. Перейдите в директорию `src`.
2. Убедитесь, что файл `input.txt` содержит корректные входные данные в указанном формате.
3. Введите входные данные в стандартный ввод 
4. Результат выполнения будет записан в файл `output.txt`.

## Пример

### Входные данные (input.txt)
```
6
31 41 59 26 41 58
```

### Выходные данные (output.txt)
```
59 58 41 41 31 26
```
