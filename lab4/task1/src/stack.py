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