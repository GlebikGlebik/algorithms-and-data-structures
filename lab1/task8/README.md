# Задача 8

## Описание

В данной задаче реализуется алгоритм пузырьковой сортировки. Алгоритм многократно сравнивает соседние элементы и меняет их местами, если они не упорядочены, тем самым упорядочивая элементы по возрастанию.

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
from time import *
import tracemalloc

tracemalloc.start()

with open ("../txtf/input.txt", "w") as f:
    n = input()
    a = input().split()
    f.write(n)
    f.write("\n")
    f.write(" ".join(a))

start = perf_counter()

with open ("../txtf/input.txt", "r") as f:
    with open ("../txtf/output.txt", "w") as g:
        n = int(f.readline())
        b = f.readline().split()
        a = [int(x) for x in b]
        for i in range(n - 1):
            m = i
            for j in range(i + 1, n):
                if a[m] > a[j]:
                    m = j
            if m != i:
                p = min(m,i) + 1
                v = max(m,i) + 1
                g.write("Swap elements at indices " + str(p) + " and " + str(v) + ".")
                g.write("\n")
            a[m], a[i] = a[i], a[m]
        g.write("No more swaps needed.")

end = perf_counter()

for q in range(n - 1):
    if a[q + 1] < a[q]:
        print("error: invalid sort")

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
26 31 41 41 58 59
```
