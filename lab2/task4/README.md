# Задача 4: Бинарный поиск в отсортированном массиве

## Описание

Данная задача включает реализацию алгоритма бинарного поиска в отсортированном массиве. Бинарный поиск — это эффективный алгоритм, используемый для поиска элемента в отсортированном массиве за логарифмическое время. Основной целью является нахождение индекса заданного элемента или определение, что элемент отсутствует в массиве.

### Описание файлов:

- **src/binary_search.py**: Основной скрипт с реализацией алгоритма бинарного поиска. Читает данные из файла `input.txt` и записывает результат в файл `output.txt`.
- **txtf/input.txt**: Входной файл, содержащий количество элементов, сам массив чисел и искомый элемент.
- **txtf/output.txt**: Выходной файл, содержащий индекс найденного элемента или `-1`, если элемент не найден.
- **tests/test_binary_search.py**: Модуль с тестами для проверки корректности работы алгоритма бинарного поиска.

## Код задачи

```python
import time
import tracemalloc

tracemalloc.start()

"""
with open ("../txtf/input.txt", "w") as f:
    n = input()
    arr = input().split()
    m = input()
    brr = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(arr))
    f.write("\n")
    f.write(m)
    f.write("\n")
    f.write(" ".join(brr))
"""

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

    return dict(sorted_array)

def binary_search(arr_dict_sorted, n, b):
    if n == 0:
        return -1
    mid = n // 2
    if list(arr_dict_sorted.values())[mid] == b:
        return list(arr_dict_sorted.keys())[mid]
    if list(arr_dict_sorted.values())[mid] > b:
        res = binary_search(dict(list(arr_dict_sorted.items())[:mid]), len(dict(list(arr_dict_sorted.items())[:mid])), b)
    if list(arr_dict_sorted.values())[mid] < b:
        res = binary_search(dict(list(arr_dict_sorted.items())[mid + 1:]), len(dict(list(arr_dict_sorted.items())[mid + 1:])), b)
    return res

with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    a1 = f.readline().split()
    arr = [int(x) for x in a1]
    m = int(f.readline())
    b1 = f.readline().split()
    brr = [int(x) for x in b1]
    arr_for_dict = []
    for i in range(len(arr)):
        arr_for_dict.append([i, arr[i]])
    arr_dict = dict(arr_for_dict)
    arr_dict_sorted = merge_sort(arr_dict)
    res = []
    for b in brr:
        res.append(binary_search(arr_dict_sorted, n, b))
        if res[-1] == None:
            res[-1] = -1
    print(res)
```

## Как запустить проект

1. **Установка зависимостей**: Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python.

2. **Запуск алгоритма бинарного поиска**:

   - Перейдите в директорию `Task4/src`.
   - Убедитесь, что файл `input.txt` содержит корректные входные данные. Формат файла:
     - Первая строка содержит число `n` (количество элементов массива).
     - Вторая строка содержит `n` целых чисел, разделенных пробелами (массив должен быть отсортирован).
     - Третья строка содержит одно число — искомый элемент.
   - Выполните команду:
     ```sh
     python binary_search.py
     ```
   - Результат будет записан в файл `output.txt`.

3. **Запуск тестов**:

   - Перейдите в директорию `Task4/tests`.
   - Выполните команду:
     ```sh
     python -m unittest test_binary_search.py
     ```
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.

## Формат входных и выходных данных

- **Входной файл (********`input.txt`********)**:

  - Первая строка: число `n` (1 ≤ `n` ≤ 10⁵) — количество элементов массива.
  - Вторая строка: `n` различных целых чисел, отсортированных по возрастанию, по модулю не превосходящих `10⁹`.
  - Третья строка: целое число `target`, по модулю не превосходящее `10⁹` — элемент, который требуется найти.

- **Выходной файл (********`output.txt`********)**:

  - Содержит одно число — индекс найденного элемента (начиная с `0`) или `-1`, если элемент не найден.

## Описание алгоритма

Алгоритм бинарного поиска работает следующим образом:

1. **Инициализация**: Определяются начальные границы поиска (`left` и `right`).
2. **Итерация**: На каждой итерации определяется средний индекс (`middle`) между `left` и `right`.
3. **Сравнение**: Проверяется, равен ли элемент на позиции `middle` искомому значению (`target`). Если да — возвращается индекс `middle`. Если нет — границы сужаются в зависимости от значения элемента (`array[middle]`), чтобы продолжить поиск в нужной половине массива.
4. **Завершение**: Если границы сходятся (`left` > `right`) и элемент не найден, возвращается `-1`.

## Тестирование

Для проверки работоспособности алгоритма реализованы юнит-тесты в файле `test_binary_search.py`. Тесты включают:

- Поиск элемента в массиве, когда элемент присутствует.
- Поиск элемента, когда его нет в массиве.
- Пустой массив.
- Массив с одним элементом (присутствует и отсутствует).
- Проверку на некорректные входные данные.

Запуск тестов позволяет убедиться в корректности работы функции для различных сценариев.

## Примеры

Пример входного файла (`input.txt`):

```
5
1 2 3 4 5
3
```

Пример выходного файла (`output.txt`) после выполнения:

```
2
```
