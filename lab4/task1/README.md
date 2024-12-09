# Задание №1 по варианту: Стек
Студент ИТМО, Дегтярь Глеб Сергеевич | 474272
## Вариант 7

## Задание
Реализовать обработку операций со стеком. Программа должна поддерживать команды добавления элемента в стек (`+ x`) и удаления верхнего элемента (`-`) с записью результата удаления.

## Input / Output

| Input              | Output |
|---------------------|--------|
| 3 \n + 5 \n + 7 \n - | 7      |
| 5 \n + 1 \n + 2 \n - \n + 3 \n - | 2 3 |
| 4 \n + 10 \n - \n + 4 \n - | 10 4 |

## Ограничения по времени и памяти

- Ограничение по времени: 1 сек.
- Ограничение по памяти: 64 МБ.

## Код задачи

```python
import time
import tracemalloc

tracemalloc.start()

start = time.perf_counter()

class Stack:
   def __init__(self):
       self.stack = []

   def pop(self):
       removed = self.stack.pop()
       return removed

   def push(self, item):
       self.stack.append(item)


with open("../txtf/input.txt", "r") as f:
    m = int(f.readline())
    with open("../txtf/output.txt", "w") as g:
        stc = Stack()
        for i in range(m):
           arr = f.readline().split()
           if arr[0] == '+':
               stc.push(arr[1])
           elif arr[0] == '-':
               g.write(str(stc.pop()) + "\n")
```

## Запуск проекта

1. Установка зависимостей: Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python.

2. Запуск алгоритма сортировки:

   - Перейдите в директорию Task1/src.
   - Убедитесь, что файл input.txt содержит корректные входные данные. 
   - Выполните команду:
          python stack.py 
     
   - Результат будет записан в файл output.txt.

3. Запуск тестов:

   - Перейдите в директорию Task1/tests.
   - Выполните команду:
          python -m unittest test_stack.py
     
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.
