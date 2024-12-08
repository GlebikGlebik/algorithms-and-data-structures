# Задание №1 по варианту : Улучшение Quick sort
Студент ИТМО, Дегтярь Глеб Сергеевич | 474272

## Вариант 7

## Задание
Реализовать алгоритм быстрой сортировки (Quick Sort), который сортирует входной массив чисел. Алгоритм рекурсивно делит массив на элементы, меньшие и большие случайного выбранного элемента, и соединяет результат.

## Input / Output

| Input    | Output |
|----------|--------|
| 5         | 1 1 3 4 5 |
| 3 1 4 1 5 |           |
| 4       | 2 5 6 9 |
| 9 2 6 5 |         |
| 6          | 1 2 3 7 8 10 |
10 7 3 2 8 1 |              |

## Ограничения по времени и памяти

- Ограничение по времени: 2 сек.
- Ограничение по памяти: 256 МБ.

## Код задачи

```python
from random import *
import time
import tracemalloc

tracemalloc.start()

"""
with open ("../txtf/input.txt", "w") as f:
    n_input = input()
    array_input = input().split()
    f.write(n_input)
    f.write("\n")
    f.write(" ".join(array_input))
"""

start = time.perf_counter()

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[randint(0, len(array) - 1)]

    left = [element for element in array if element < pivot]
    middle = [element for element in array if element == pivot]
    right = [element for element in array if element > pivot]

    return quick_sort(left) + middle + quick_sort(right)

"""
with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    array = f.readline().split()
    array = [int(x) for x in array]
    res = quick_sort(array)

with open("../txtf/output.txt", "w") as f:
    res = [str(x) for x in res]
    s = " ".join(res)
    f.write(s)
"""

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()
```

## Запуск проекта

1. Клонируйте репозиторий:
```bash
    git clone https://github.com/username/repository-name.git
```
2. Перейдите в папку с проектом:
```bash
    cd repository-name/lab1
```
3. Запустите программу:
```bash
    python src/main.py
```
4. Запуск тестов:
```bash
    python -m unittest discover tests/
```
## Тестирование
Для запуска тестов выполните:
```bash
python test_random_quick_sort.py
```
