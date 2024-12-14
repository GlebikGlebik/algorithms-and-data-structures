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

if __name__ == "__main__":
    decorate(task=1, task_name="stack")
