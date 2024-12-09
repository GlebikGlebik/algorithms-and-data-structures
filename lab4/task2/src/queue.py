import time
import tracemalloc

tracemalloc.start()

start = time.perf_counter()

class Queue:
   def __init__(self):
       self.queue = []

   def pop(self):
       if len(self.queue) == 0:
           return None
       res = self.queue.pop(0)
       return res

   def push(self, item):
       self.queue.append(item)


with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
    q = Queue()
    with open("../txtf/output.txt", "w") as g:
        for i in range(n):
           arr = f.readline().split()
           if arr[0] == '+':
               q.push(arr[1])
           elif arr[0] == '-':
               g.write(str(q.pop()) + "\n")

end = time.perf_counter()

print("Время работы: ", end - start, "секунд")
current, peak = tracemalloc.get_traced_memory()
print(f"Пиковая память: {peak / 2**20:.2f} MB")
tracemalloc.stop()