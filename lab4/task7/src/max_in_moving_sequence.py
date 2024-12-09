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
