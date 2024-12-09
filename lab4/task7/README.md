# Задание №7 по варианту : Максимум в движущейся последовательности
Студент ИТМО, Дегтярь Глеб Сергеевич | 474272

## Вариант 7

## Задание
Реализовать алгоритм нахождения максимума в плавающем "окне" списка. 

## Input / Output

| Input    | Output |
|----------|--------|
| 5   | 1 1 3 4 5 |
| 3 1 4 1 5 | |
| 4   | 2 5 6 9 |
| 9 2 6 5 | |
| 6   | 1 2 3 7 8 10 |
| 10 7 3 2 8 1 | | 

## Ограничения по времени и памяти

- Ограничение по времени: 2 сек.
- Ограничение по памяти: 256 МБ.

## Код задачи

```python
import time
import tracemalloc

tracemalloc.start()

start = time.perf_counter()

class Queue:
    def __init__(self):
        self.queue = []
        self.max_queue = []  # Стек для хранения максимумов

    def pop(self):
        if self.queue:
            removed = self.queue.pop(0)
            if removed == self.max_queue[0]:
                self.max_queue.pop(0)  # Удаляем максимум из max_queue
            return removed
        return None

    def push(self, item):
        self.queue.append(item)
        # Обновляем max_queue
        while self.max_queue and self.max_queue[-1] < item:
            self.max_queue.pop()  # Удаляем все меньшие элементы из max_queue
        self.max_queue.append(item)

with open("../txtf/input.txt", "r") as f:
    n = int(f.readline().strip())
    q = Queue()
    with open("../txtf/output.txt", "w") as g:
        arr = list(map(int, f.readline().split()))
        m = int(f.readline())
        for i in range(n):
            if len(q.queue) < m:
                q.push(arr[i])
            else:
                g.write(str(q.max_queue[0]) + ' ')  # Записываем текущий максимум
                q.pop()  # Удаляем элемент
                q.push(arr[i])  # Добавляем новый элемент
        if len(q.queue) == m:  # Записываем максимум для последней группы
            g.write(str(q.max_queue[0]) + ' ')

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()
```

## Запуск проекта

1. Установка зависимостей: Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python.

2. Запуск алгоритма сортировки:

   - Перейдите в директорию Task7/src.
   - Убедитесь, что файл input.txt содержит корректные входные данные. 
   - Выполните команду:
          python max_in_moving_sequence.py 
     
   - Результат будет записан в файл output.txt.

3. Запуск тестов:

   - Перейдите в директорию Task7/tests.
   - Выполните команду:
          python -m unittest test_max_in_moving_sequence.py
     
   - Все тесты должны завершиться успешно, подтверждая корректность работы алгоритма.
