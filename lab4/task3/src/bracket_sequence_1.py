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