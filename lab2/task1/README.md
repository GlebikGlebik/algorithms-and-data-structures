# Задача 1: Реализация Сортировки Слиянием

## Описание

Данная задача включает реализацию алгоритма сортировки слиянием (Merge Sort), который использует метод "Разделяй и властвуй" для сортировки массива целых чисел. Основной целью является реализация эффективного алгоритма для сортировки входных данных, представленных в виде массива, а также сохранение результата в выходной файл.

### Описание файлов:

- **src/merge_sort.py**: Основной скрипт с реализацией алгоритма сортировки слиянием. Читает данные из файла `input.txt` и записывает отсортированный массив в файл `output.txt`.
- **src/input.txt**: Входной файл, содержащий количество элементов и сам массив чисел, который необходимо отсортировать.
- **src/output.txt**: Выходной файл, содержащий отсортированный массив.
- **tests/test_merge_sort.py**: Модуль с тестами для проверки корректности работы алгоритма сортировки.

 ## Код задачи

```python
import time
import tracemalloc

tracemalloc.start()

"""
with open ("../txtf/input.txt", "w") as f:
    n = input()
    a = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))
"""

start = time.perf_counter()

def merge(L, R):
    res = []
    i, j = 0, 0
    n, m = len(L), len(R)
    while i < n and j < m:
        if L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    while j < m:
        res.append(R[j])
        j += 1
    while i < n:
        res.append(L[i])
        i += 1
    return res

def merge_sort(A):
    if len(A) <= 1:
        return A
    q = len(A) // 2
    left = merge_sort(A[:q])
    right = merge_sort(A[q:])
    return merge(left, right)

with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    A1 = f.readline().split()
    A = [int(x) for x in A1]
    res = merge_sort(A)


with open("../txtf/output.txt", "w") as f:
    res = [str(x) for x in res]
    s = " ".join(res)
    f.write(s)

end = time.perf_counter()


print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()
```

## Как запустить проект

1. **Установка зависимостей**: Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python.


2. **Запуск алгоритма сортировки**:

   - Перейдите в директорию `Task-1/src`.
   - Убедитесь, что файл `input.txt` содержит корректные входные данные. Формат файла:
     - Первая строка содержит число `n` (количество элементов массива).
     - Вторая строка содержит `n` целых чисел, разделенных пробелами.
   - Выполните команду:
     ```sh
     python merge_sort.py
     ```
   - Результат будет записан в файл `output.txt`.

3. **Запуск тестов**:

   - Перейдите в директорию `Task-1/tests`.
   - Выполните команду:
     ```sh
     python -m unittest test_merge_sort.py
     ```
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.

## Формат входных и выходных данных

- **Входной файл (****`input.txt`****)**:

  - Первая строка: число `n` ( ≤ `n` ≤ 2 ⋅ 10⁴) — количество элементов массива.
  - Вторая строка: `n` различных целых чисел, по модулю не превосходящих `10⁹`.

- **Выходной файл (****`output.txt`****)**:

  - Содержит одну строку с отсортированным массивом, где элементы разделены пробелами.

## Описание алгоритма

Алгоритм сортировки слиянием состоит из следующих этапов:

1. **Разделение**: Деление массива на две части, пока размер подмассивов не станет равным единице.
2. **Властвование**: Рекурсивная сортировка подмассивов.
3. **Комбинирование**: Слияние двух отсортированных подмассивов в один.

Функция `merge` используется для объединения двух отсортированных подмассивов в один, а `merge_sort` — для рекурсивного разбиения и сортировки.

## Тестирование

Для проверки работоспособности алгоритма реализованы юнит-тесты в файле `test_merge_sort.py`. Тесты включают:

- Сортировку обычных массивов.
- Проверку на уже отсортированный массив.
- Обратный порядок элементов.
- Пустой массив и массив с одним элементом.
- Проверку на большие числа и некорректные входные данные.

Запуск тестов позволяет убедиться в корректности работы функции для различных сценариев.

## Примеры

Пример входного файла (`input.txt`):

```
6
12 11 13 5 6 7
```

Пример выходного файла (`output.txt`) после сортировки:

```
5 6 7 11 12 13
```