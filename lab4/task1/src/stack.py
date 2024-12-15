import sys
import os
from lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        removed = self.stack.pop()
        return removed

    def push(self, item):
        self.stack.append(item)


def main():
    input_file = read_input(1)
    m = int(input_file[0])
    pops = []
    stc = Stack()
    for i in input_file:
        arr = i.split()
        if arr[0] == '+':
            stc.push(arr[1])
        elif arr[0] == '-':
            pops.append(str(stc.pop()))

    write_output(1, *pops)
if __name__ == "__main__":
    decorate(task=1, task_name="stack")
