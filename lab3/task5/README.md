# Задание №5 по выбору : Индекс Хирша
Студент ИТМО, Дегтярь Глеб Сергеевич | 474272

## Вариант 7

## Задание
Посчитать индекс Хирша учёного. 

## Input / Output

| Input              | Output      |
|--------------------|-------------|
| 3,0,6,1,5 | 3 |
| 1,3,1 | 1 |           |

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
    array_input = input().split(',')
    f.write(" ".join(array_input))
"""

start = time.perf_counter()

def h_index(array):
    h_indexes = []
    for i in range(len(array)):
        count = 0
        for j in range(1, len(array)):
            if array[i] >= array[j]:
                count += 1
        h_indexes.append(count)
    return max(h_indexes) - 1

"""
with open("../txtf/input.txt", "r") as f:
    array = list(map(int,f.readline().split()))
    res = h_index(array)

with open("../txtf/output.txt", "w") as f:
    f.write(str(res))
"""

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()
```

## Запуск проекта

1. Установка зависимостей: Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python.

2. Запуск алгоритма сортировки:

   - Перейдите в директорию Task5/src.
   - Убедитесь, что файл input.txt содержит корректные входные данные. 
   - Выполните команду:
          python h_index.py 
     
   - Результат будет записан в файл output.txt.

3. Запуск тестов:

   - Перейдите в директорию Task5/tests.
   - Выполните команду:
          python -m unittest test_h_index.py
     
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.
