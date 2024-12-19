import sys
import os
from lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Stack:
    def __init__(self):
       self.stack = []
       self.s = []
       self.input_file = read_input(3)

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

    def result(self):
        answers = []
        for i in self.input_file[1:]:
            answers.append(self.right_pos(i))
        return answers

def main():
    stc = Stack()
    res = stc.result()
    write_output(3, *res)
    [print(i) for i in res]

if __name__ == '__main__':
    decorate(task=3, task_name='bracket_sequence_1')

