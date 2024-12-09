# Задание №3 по варианту: Скобочная последовательность. Версия 1
Студент ИТМО, Дегтярь Глеб Сергеевич | 474272
## Вариант 7

## Задание
Реализовать проверку корректности скобочной последовательности. Программа должна проверять строки на соответствие правилам открывающихся и закрывающихся скобок.

## Input / Output

| Input           | Output |
|------------------|--------|
| 3 \n () \n (] \n ([)] | YES NO NO |
| 2 \n [] \n (()()) | YES YES |
| 1 \n ([{}])       | YES    |

## Ограничения по времени и памяти

- Ограничение по времени: 1 сек.
- Ограничение по памяти: 64 МБ.

```python
import time
import tracemalloc

tracemalloc.start()

start = time.perf_counter()

class Stack:
   def __init__(self):
       self.stack = []

   def pop(self):
       if len(self.stack) == 0:
           return None
       removed = self.stack.pop()
       return removed

   def push(self, item):
       self.stack.append(item)

def right_pos(A):
   stc = Stack()
   if s[0] == ']' or s[0] == ')' or s.count(')') != s.count('(') or s.count(']') != s.count('['):
       return "NO"
   for x in s:
       if x == '(' or x == '[':
           stc.push(x)
       else:
           nr = stc.pop()
           if (x == ']' and nr == '(') or (x == ')' and nr == '['):
               return "NO"
   return "YES"

with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    with open("../txtf/output.txt", "w", encoding= 'UTF-8') as g:
        for i in range(n):
           s = f.readline().strip()
           g.write(right_pos(s) + '\n')


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
          python bracket_sequence_1.py 
     
   - Результат будет записан в файл output.txt.

3. Запуск тестов:

   - Перейдите в директорию Task3/tests.
   - Выполните команду:
          python -m unittest test_bracket_sequence_1.py
     
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.

---
