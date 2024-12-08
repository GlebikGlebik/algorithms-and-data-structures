# Задача 9: Метод штрассена для умножения матриц

## Описание

Данная задача включает реализацию алгоритма перемножения матриц методом Штрассена. Данный алгоритм позволяет ускорить операцию умножения матириц за счет разбития матриц на подматрицы и уменьшения количества внутренних переменожений. Основной целью является написание программы для реализации алгоритма.

### Описание файлов:

- **src/Strassens_method_for_matrix_multiplication.py**: Основной скрипт с реализацией алгоритма бинарного поиска. Читает данные из файла `input.txt` и записывает результат в файл `output.txt`.
- **txtf/input.txt**: Входной файл, содержащий количество элементов, сам массив чисел и искомый элемент.
- **txtf/output.txt**: Выходной файл, содержащий индекс найденного элемента или `-1`, если элемент не найден.
- **tests/test_Strassens_method_for_matrix_multiplication.py**: Модуль с тестами для проверки корректности работы алгоритма бинарного поиска.

## Код задачи

```python
from math import *
import time
import tracemalloc

tracemalloc.start()

"""
with open ("../txtf/input.txt", "w") as f:
    n = input()
    a = input().split()
    b = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))
    f.write("\n")
    f.write(" ".join(b))
"""

start = time.perf_counter()

def strassen_multiplication(a, b, n):
    """
    Умножение матриц методом Штрасса.
    :param a: первая матрица
    :param b: вторая матрица
    :param n: порядок матриц (размерность)
    :return: произведение матриц a и b
    """
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    mid = n // 2

    # Разделяем матрицы на 4 подматрицы
    a11 = [row[:mid] for row in a[:mid]]
    a12 = [row[mid:] for row in a[:mid]]
    a21 = [row[:mid] for row in a[mid:]]
    a22 = [row[mid:] for row in a[mid:]]

    b11 = [row[:mid] for row in b[:mid]]
    b12 = [row[mid:] for row in b[:mid]]
    b21 = [row[:mid] for row in b[mid:]]
    b22 = [row[mid:] for row in b[mid:]]

    # Вычисляем 7 произведений
    m1 = strassen_multiplication(matrix_sum(a11, a22), matrix_sum(b11, b22), mid)
    m2 = strassen_multiplication(matrix_sum(a21, a22), b11, mid)
    m3 = strassen_multiplication(a11, matrix_minus(b12, b22), mid)
    m4 = strassen_multiplication(a22, matrix_minus(b21, b11), mid)
    m5 = strassen_multiplication(matrix_sum(a11, a12), b22, mid)
    m6 = strassen_multiplication(matrix_minus(a21, a11), matrix_sum(b11, b12), mid)
    m7 = strassen_multiplication(matrix_minus(a12, a22), matrix_sum(b21, b22), mid)

    # Собираем результаты в итоговую матрицу
    c11 = matrix_sum(matrix_minus(matrix_sum(m1, m4), m5), m7)
    c12 = matrix_sum(m3, m5)
    c21 = matrix_sum(m2, m4)
    c22 = matrix_sum(matrix_minus(matrix_sum(m1, m3), m2), m6)

    # Формируем новую матрицу
    new_matrix = []
    for i in range(mid):
        new_matrix.append(c11[i] + c12[i])
    for i in range(mid):
        new_matrix.append(c21[i] + c22[i])

    return new_matrix

def matrix_maker(a, n):
    matrix = []
    for i in range(0, len(a), n):
        matrix.append(a[i: i + n])
    return matrix

def matrix_sum(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrix_minus(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def pad_matrix(matrix, new_size):
    padded = [[0] * new_size for _ in range(new_size)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            padded[i][j] = matrix[i][j]
    return padded

def closest_power_of_two(n):
    if n <= 1:
        return 1
    return 2 ** ceil(log2(n))

"""
with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    a_input = list(map(int, f.readline().split()))
    b_input = list(map(int, f.readline().split()))

    a = matrix_maker(list(map(int, a_input)), n)
    b = matrix_maker(list(map(int, b_input)), n)

    new_size = closest_power_of_two(n)

    a_padded = pad_matrix(a, new_size)
    b_padded = pad_matrix(b, new_size)

    result = strassen_multiplication(a_padded, b_padded, new_size)

    result = [row[:n] for row in result[:n]]

with open("../txtf/output.txt", "w") as f:
    for row in result:
        row = [str(x) for x in row]
        f.write(" ".join(row))
        f.write("\n")
"""

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()
```

## Как запустить проект

1. **Установка зависимостей**: Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python.

2. **Запуск алгоритма бинарного поиска**:

   - Перейдите в директорию `Task9/src`.
   - Убедитесь, что файл `input.txt` содержит корректные входные данные. Формат файла:
     - Первая строка содержит число `n` (количество элементов массива).
     - Вторая строка содержит `n` целых чисел, разделенных пробелами (массив должен быть отсортирован).
     - Третья строка содержит одно число — искомый элемент.
   - Выполните команду:
     ```sh
     python Strassens_method_for_matrix_multiplication.py
     ```
   - Результат будет записан в файл `output.txt`.

3. **Запуск тестов**:

   - Перейдите в директорию `Task9/tests`.
   - Выполните команду:
     ```sh
     python -m unittest test_Strassens_method_for_matrix_multiplication.py
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

Для проверки работоспособности алгоритма реализованы юнит-тесты в файле `test_Strassens_method_for_matrix_multiplication.py`. Тесты включают:

- Поиск элемента в массиве, когда элемент присутствует.
- Поиск элемента, когда его нет в массиве.
- Пустой массив.
- Массив с одним элементом (присутствует и отсутствует).
- Проверку на некорректные входные данные.

Запуск тестов позволяет убедиться в корректности работы функции для различных сценариев.

## Примеры

Пример входного файла (`input.txt`):

```
3
1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1
```

Пример выходного файла (`output.txt`) после выполнения:

```
30 24 18
84 69 54
138 114 90
```
