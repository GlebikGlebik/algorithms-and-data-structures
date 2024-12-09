# Задание №5 по варианту: Стек с максимумом
Студент ИТМО, Дегтярь Глеб Сергеевич | 474272
## Вариант 7

## Задание
Реализовать стек с поддержкой операции max. Программа должна выполнять команды добавления (`push x`), удаления (`pop`), и получения максимума (`max`).

## Input / Output

| Input                     | Output |
|----------------------------|--------|
| 5 \n push 1 \n push 2 \n max \n pop \n max | 2 1    |
| 3 \n push 3 \n max \n pop | 3       |
| 4 \n push 5 \n push 5 \n max \n pop | 5       |

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
       self.max = None
       self.stack_max = []

   def pop(self):
       """Если в стеки не осталось элементов, то максимумом берется последний элемент из stack_max"""
       if len(self.stack) == 0:
           self.max = None
           return None
       removed = self.stack.pop()
       if removed == self.max:
           self.stack_max.pop()
           self.max = self.stack_max[-1]
       return removed

   def push(self, item):
       """Если мы добавили в стек 1‑й элемент, он становится максимумом, если нет, то новый элемент сравнивается с текущим максимумом"""
       self.stack.append(item)
       if len(self.stack) == 1 or item > self.max:
           self.max = item
           self.stack_max.append(item)

with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    stc = Stack()
    with open("../txtf/output.txt", "w") as g:
        for i in range(n):
           d = f.readline().split()
           if d[0] == 'push':
               stc.push(int(d[1]))
           elif d[0] == 'pop':
               stc.pop()
           elif d[0] == 'max':
               g.write(str(stc.max) + "\n")

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
          python stack_with_max.py 
     
   - Результат будет записан в файл output.txt.

3. Запуск тестов:

   - Перейдите в директорию Task5/tests.
   - Выполните команду:
          python -m unittest test_stack_with_max.py
     
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.

---
