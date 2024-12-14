import sys
import os
from lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Stack:
   def __init__(self):
       self.stack = []
       self.s = []

   def pop(self):
       if len(self.stack) == 0:
           return None
       removed = self.stack.pop()
       return removed

   def push(self, item):
       self.stack.append(item)

   def right_pos(self, s):
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

def main():
    stc = Stack()
    with open("../txtf/input.txt", "r") as f:
        n = int(f.readline())
        with open("../txtf/output.txt", "w", encoding= 'UTF-8') as g:
            for i in range(n):
               s = f.readline().strip()
               g.write(stc.right_pos(s) + '\n')

if __name__ == '__main__':
    decorate(task=3, task_name='bracket_sequence_1')

