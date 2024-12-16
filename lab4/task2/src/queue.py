import sys
import os
from lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Queue:
    def __init__(self):
        self.queue = []
        self.input_file = read_input(2)
        self.n = int(self.input_file[0])

    def pop(self):
        if len(self.queue) == 0:
            return None
        res = self.queue.pop(0)
        return res

    def push(self, item):
        self.queue.append(item)


    def result(self):
        pops = []
        for i in self.input_file:
            arr = i.split()
            if arr[0] == '+':
                self.push(arr[1])
            elif arr[0] == '-':
                pops.append(str(self.pop()))
        return pops

def main():
    q = Queue()
    res = q.result()
    write_output(2, *res)

if __name__ == '__main__':
    decorate(task=2, task_name='queue')
