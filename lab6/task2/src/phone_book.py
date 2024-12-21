import sys
import os

from lab6.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class PhoneBook:
    def __init__(self):
        self.input_file = read_input(2)
        self.n = self.input_file[0]
        self.array = []
        [self.array.append(i.split()) for i in self.input_file[1:]]
        self.phone_book = []

    def add(self, number, name):
        for i in self.phone_book:
            if i[0] == number:
                self.dell(number)
        self.phone_book.append((number, name))

    def dell(self, number):
        for i in self.phone_book:
            if i[0] == number:
                self.phone_book.remove(i)

    def find(self, number):
        for i in self.phone_book:
            if i[0] == number:
                return i[1]
        return 'not found'

def main():
    book = PhoneBook()
    res = []
    for row in book.array:
        if row[0] == 'add':
            book.add(row[1], row[2])
        elif row[0] == 'find':
            res.append(book.find(row[1]))
        elif row[0] == 'del':
            book.dell(row[1])

    write_output(2, *res)
    [print(i) for i in res]

if __name__ == '__main__':
    decorate(task=2, task_name='phone_book')