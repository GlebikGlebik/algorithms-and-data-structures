# Задание №9 по варианту : Ближайшие точки к началу координат 
Студент ИТМО, Дегтярь Глеб Сергеевич | 474272

## Вариант 7

## Задание
Найти расстояние между двумя ближайшими точками

## Input / Output

| Input              | Output      |
|--------------------|-------------|
| 2 | 5.0|
| 0 0 |         
| 3 4  | 

## Ограничения по времени и памяти

- Ограничение по времени: 10 сек.
- Ограничение по памяти: 256 МБ.

## Код задачи

```python
import time
import tracemalloc
import math

tracemalloc.start()

"""
with open ("../txtf/input.txt", "w") as f:
    n_input = input()
    f.write(n_input)
    f.write("\n")
    for i in range(int(n_input)):
        array_input = input().split()
        f.write(" ".join(array_input))
        f.write("\n")
"""

start = time.perf_counter()

def nearest_point(arr_of_points, n):
    min_dist = 10**9
    index1 = 0
    index2 = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if math.sqrt((arr_of_points[i][0] - arr_of_points[j][0])**2 + (arr_of_points[i][1] - arr_of_points[j][1])**2) < min_dist:
                min_dist = math.sqrt((arr_of_points[i][0] - arr_of_points[j][0])**2 + (arr_of_points[i][1] - arr_of_points[j][1])**2)
                index1 = i
                index2 = j
    indexes = (index1, index2)
    return indexes, min_dist

"""
with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    arr_of_points = {}
    for i in range(n):
        point = tuple(map(int, f.readline().split()))
        arr_of_points[i] = point
    res, min_dist = nearest_point(arr_of_points, n)

with open("../txtf/output.txt", "w") as f:
    point1 = str(arr_of_points[res[0]])
    point2 = str(arr_of_points[res[1]])
    f.write('closest points:')
    f.write('\n')
    f.write(point1 + ',' + point2)
    f.write('\n')
    f.write('distance between points: ')
    f.write('\n')
    f.write(str(min_dist))
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

   - Перейдите в директорию Task9/src.
   - Убедитесь, что файл input.txt содержит корректные входные данные. 
   - Выполните команду:
          python nearest_points.py 
     
   - Результат будет записан в файл output.txt.

3. Запуск тестов:

   - Перейдите в директорию Task9/tests.
   - Выполните команду:
          python -m unittest test_nearest_points.py
     
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.
