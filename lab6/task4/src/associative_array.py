import sys
import os

from lab6.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class AssociativeArray:
    def __init__(self):
        self.input_file = read_input(4)
        self.n = self.input_file[0]
        self.array = []
        [self.array.append(i.split()) for i in self.input_file[1:]]
        self.ass_array = {}

    def put(self, key, value):
        self.ass_array[key] = value

    def get(self, key):
        for i in self.ass_array.keys():
            if i == key:
                return self.ass_array[i]
        return '<None>'

    def prev(self, key):
        if key in self.ass_array:
            keys = list(self.ass_array.keys())
            idx = keys.index(key)
            if idx > 0:
                return self.ass_array[keys[idx - 1]]
            else:
                return "<none>"
        else:
            return "<none>"

    def next(self, key):
        if key in self.ass_array:
            keys = list(self.ass_array.keys())
            idx = keys.index(key)
            if idx < len(keys) - 1:
                return self.ass_array[keys[idx + 1]]
            else:
                return "<none>"
        else:
            return "<none>"

    def delete(self, key):
        del self.ass_array[key]

def main():
    ass = AssociativeArray()
    res = []
    for i in ass.array:
        if i[0] == 'put':
            ass.put(i[1], i[2])
        elif i[0] == 'get':
            res.append(ass.get(i[1]))
        elif i[0] == 'prev':
            res.append(ass.prev(i[1]))
        elif i[0] == 'next':
            res.append(ass.next(i[1]))
        elif i[0] == 'delete':
            ass.delete(i[1])

    write_output(4, *res)
    [print(i) for i in res]
    print()

if __name__ == '__main__':
    decorate(task=4, task_name='associative_array')