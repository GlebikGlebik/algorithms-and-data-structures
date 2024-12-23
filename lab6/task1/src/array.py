import sys
import os
from lab6.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class Set:
    def __init__(self):
        self.data = {}

    def add(self, x):
        # Добавление элемента в множество
        self.data[x] = True

    def remove(self, x):
        # Удаление элемента из множества
        if x in self.data:
            del self.data[x]

    def exists(self, x):
        # Проверка существования элемента в множестве
        return x in self.data

def result(operations):
    arr = Set()
    results = []
    for operation in operations:
        x = int(operation[1])
        if operation[0] == 'A':
            arr.add(x)
        elif operation[0] == 'D':
            arr.remove(x)
        elif operation[0] == '?':
            if arr.exists(x):
                results.append('Y')
            else:
                results.append('N')
    return results

def main():
    input_file = read_input(1)
    operations = []
    [operations.append(i.split()) for i in input_file[1:]]

    res = result(operations)

    write_output(1, *res)
    [print(i) for i in res]


if __name__ == '__main__':
    decorate(1, 'array')