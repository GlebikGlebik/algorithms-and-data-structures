# Задание №3 по выбору: Сортировка пугалом
Студент ИТМО, Дегтярь Глеб Сергеевич | К3141

## Вариант 7

## Задание
Алгоритм организует элементы массива в группы, сортирует их в обратном порядке и проверяет, упорядочены ли они правильно.

## Input / Output

| Input    | Output |
|----------|--------|
| 5 2 | ДА| 
| 5 1 3 2 4 |  |
| 6 3 | НЕТ |
| 9 8 7 6 5 4 |  |
| 4 2 | ДА |
| 3 2 4 1 |  |

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
    n_input, k_input = input().split()
    array_input = input().split()
    f.write(n_input + " " + k_input)
    f.write("\n")
    f.write(" ".join(array_input))
"""

start = time.perf_counter()

def scarecrow_sort(n, k, arr):
    """
    :param n: Количество матрёшек.
    :param k: Размах рук (расстояние для обмена).
    :param arr: Список размеров матрёшек.
    :return: True, если сортировка возможна, иначе False.
    :raises ValueError: Если длина массива не равна n.
    """

    # Создаём список групп, где каждая группа соответствует позиции по модулю k
    groups = [[] for _ in range(k)]
    for index in range(n):
        groups[index % k].append(arr[index])

    # Сортируем каждую группу по неубыванию
    for group in groups:
        group.sort()

    # Сортированный массив для сравнения
    sorted_arr = sorted(arr)

    # Проверяем, можно ли собрать отсортированный массив из отсортированных групп
    for index in range(n):
        group_index = index % k
        element_index = index // k
        if element_index >= len(groups[group_index]):
            # Это условие обычно не должно возникать, но добавляем для безопасности
            return False
        actual_value = groups[group_index][element_index]
        expected_value = sorted_arr[index]
        if actual_value != expected_value:
            return False
    return True

"""
with open("../txtf/input.txt", "r") as f:
    n, k = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))
    res = scarecrow_sort(n, k, arr)

with open("../txtf/output.txt", "w", encoding= "UTF-8") as f:
    if res:
        f.write("ДА")
    else:
        f.write("НЕТ")
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

   - Перейдите в директорию Task3/src.
   - Убедитесь, что файл input.txt содержит корректные входные данные. 
   - Выполните команду:
          python scarecrow_sort.py 
     
   - Результат будет записан в файл output.txt.

3. Запуск тестов:

   - Перейдите в директорию Task3/tests.
   - Выполните команду:
          python -m unittest test_scarecrow_sort.py
     
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.
