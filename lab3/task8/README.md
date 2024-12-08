# Задание №8 по выбору : Ближайшие точки к началу координат 
Студент ИТМО, Дегтярь Глеб Сергеевич | 474272

## Вариант 7

## Задание
Найти k ближайших к началу координат точек.

## Input / Output

| Input              | Output      |
|--------------------|-------------|
| 2 1 | [-2,2] |
| 1 3 |         
| -2 2 | 

## Ограничения по времени и памяти

- Ограничение по времени: 2 сек.
- Ограничение по памяти: 256 МБ.

## Код задачи

```python
import time
import tracemalloc
import math

tracemalloc.start()

"""
with open ("../txtf/input.txt", "w") as f:
    n_input, k_input = map(str, input().split())
    f.write(n_input + ' ' + k_input)
    f.write("\n")
    for i in range(int(n_input)):
        array_input = input().split()
        f.write(" ".join(array_input))
        f.write("\n")
"""

start = time.perf_counter()

def nearest_points_to_the_origin(arr_of_points, n, k):
    closest_points = []
    point = 0
    for i in range(k):
        min_dist = 10**9
        for j in range(len(arr_of_points)):
            if math.sqrt((0 - arr_of_points[j][0])**2 + (0 - arr_of_points[j][1])**2) < min_dist:
                min_dist = math.sqrt((0 - arr_of_points[j][0])**2 + (0 - arr_of_points[j][1])**2)
                point = j
        closest_points.append(arr_of_points[point])
        del arr_of_points[point]
    return closest_points

"""
with open("../txtf/input.txt", "r") as f:
    n, k = map(int, f.readline(3).split())
    arr_of_points = []
    for i in range(n + 1):
        point = list(map(int, f.readline().split()))
        arr_of_points.append(point)
    del arr_of_points[0]
    res = nearest_points_to_the_origin(arr_of_points, n, k)

with open("../txtf/output.txt", "w") as f:
    f.write('closest points to the origin:')
    f.write('\n')
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

   - Перейдите в директорию Task8/src.
   - Убедитесь, что файл input.txt содержит корректные входные данные. 
   - Выполните команду:
          python nearest_points_to_the_origin.py 
     
   - Результат будет записан в файл output.txt.

3. Запуск тестов:

   - Перейдите в директорию Task8/tests.
   - Выполните команду:
          python -m unittest test_nearest_points_to_the_origin.py
     
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.
