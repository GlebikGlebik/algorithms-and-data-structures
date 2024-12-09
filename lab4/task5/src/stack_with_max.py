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