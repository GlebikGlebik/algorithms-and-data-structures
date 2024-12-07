# Задача 1: Сортировка вставками

## Описание

В данной задаче реализуется алгоритм сортировки вставками. Алгоритм работает путём прохода по элементам массива и вставки каждого элемента в его правильную позицию среди уже отсортированных элементов.

### Формат входных данных
- Входные данные находятся в файле `input.txt`.
- Первая строка содержит одно число `n` (1 ≤ n ≤ 1000) — количество элементов в массиве.
- Вторая строка содержит `n` целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле `output.txt` должен содержаться отсортированный массив. Все числа должны быть разделены ровно одним пробелом.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Код задачи

```python
def insertion_sort(arr):
    """
    Функция для сортировки массива методом вставки.

    Алгоритм сортирует элементы, перенося каждый новый элемент в отсортированную часть массива.

    :param arr: Список целых чисел для сортировки.
    :return: Отсортированный по возрастанию список.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы, которые больше key, на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == '__main__':
    with open('input.txt') as f:
        n, massive = f.readlines()
    array = insertion_sort(list(map(int, massive.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)
```

## Запуск проекта

1. Перейдите в директорию `src`.
2. Убедитесь, что файл `input.txt` содержит корректные входные данные в указанном формате.
3. Введите входные данные в стандартный ввод
5. Результат выполнения будет записан в файл `output.txt`.

## Тестирование

Для проверки корректности работы программы выполните тесты, находящиеся в директории `tests`.

1. Перейдите в директорию `tests`.
2. Выполните команду:
   ```sh
   python -m unittest test_insertion_sort.py
   ```

### Тесты

```python
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

with open ("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    a = f.readline().split()
    a = [int(x) for x in a]
    for i in range(1, n, 1):
        for j in range (0, i, 1):
            if a[i] < a[i - 1]:
                if a[j] > a[i]:
                    p = a[j]
                    a[j] = a[i]
                    a[i] = p

for q in range(n - 1):
    if a[q + 1] < a[q]:
        print("error: invalid sort")

end = time.perf_counter()

with open ("../txtf/output.txt", "w") as f:
    a = [str(x) for x in a ]
    f.write(" ".join(a))

print("Время работы: ", end - start, "секунд")

current, peak = tracemalloc.get_traced_memory()

print(f"Пиковая память: {peak / 2**20:.2f} MB")

tracemalloc.stop()
```

## Пример

### Входные данные (input.txt)
```
6
31 41 59 26 41 58
```

### Выходные данные (output.txt)
```
26 31 41 41 58 59
```
