import sys
import os

from lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Stack:
    def __init__(self):
        self.input_file = read_input(1)
        self.array = self.input_file[1:]
        self.stack = []

    def pop(self):
        removed = self.stack.pop()
        return removed

    def push(self, item):
        self.stack.append(item)


    def result(self):
        pops = []
        for i in self.array:
            arr = i.split()
            if arr[0] == '+':
                self.push(arr[1])
            elif arr[0] == '-':
                pops.append(str(self.pop()))
        return pops

def main():
    stc = Stack()
    pops = stc.result()
    write_output(1, *pops)
    return pops

if __name__ == "__main__":
    decorate(task=1, task_name="stack")
