import sys
import os
from lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

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


def main():
    input_file = read_input(5)
    n = int(input_file[0])
    stc = Stack()
    res = []
    for i in input_file[1:]:
       d = i.split()
       if d[0] == 'push':
           stc.push(int(d[1]))
       elif d[0] == 'pop':
           stc.pop()
       elif d[0] == 'max':
           res.append(str(stc.max))
    write_output(5, *res)

if __name__ == "__main__":
    decorate(task=5, task_name="stack_with_max")