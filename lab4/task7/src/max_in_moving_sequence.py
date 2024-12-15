import sys
import os
from lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

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

def main():
    input_file = read_input(7)
    n = int(input_file[0])
    arr = list(map(int, input_file[1].split()))
    m = int(input_file[2])
    q = Queue()
    res = []
    for i in range(n):
        if len(q.queue) < m:
            q.push(arr[i])
        else:
            res.append(str(q.max_queue[0]))  # Записываем текущий максимум
            q.pop()  # Удаляем элемент
            q.push(arr[i])  # Добавляем новый элемент
    if len(q.queue) == m:  # Записываем максимум для последней группы
        res.append(str(q.max_queue[0]))
    write_output(7, ' '.join(res))

if __name__ == "__main__":
    decorate(task=7, task_name="max_in_moving_sequence")