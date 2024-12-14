import sys
import os
from lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

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


def main():
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


if __name__ == '__main__':
    decorate(task=2, task_name='queue')
