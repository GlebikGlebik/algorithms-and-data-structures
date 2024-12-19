import sys
import os
from lab5.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class TreeHeightCalculator:
    def __init__(self):
        input_file = read_input(task=2)
        self.n = int(input_file[0])
        self.parents = [int(i) for i in input_file[1].split(' ')]
        self.tree = [[] for _ in range(self.n)]
        self.root = -1

    def height(self, node):
        if not self.tree[node]:
            return 1
        max_h = 0
        for child in self.tree[node]:
            max_h = max(max_h, self.height(child))
        return max_h + 1

    def tree_height(self, n, parents):
        """
        Вычисляет высоту дерева.

        :param n: Количество узлов.
        :param parents: Список родителей для каждого узла (индекс = узел, значение = родитель).
        :return: Высота дерева.
        """
        self.tree = [[] for _ in range(n)]
        self.root = -1

        for i in range(n):
            if parents[i] == -1:
                self.root = i
            else:
                self.tree[parents[i]].append(i)
        return self.height(self.root)


def main():
    tree = TreeHeightCalculator()
    res = tree.tree_height(tree.n, tree.parents)
    write_output(2, res)
    print(res)
    print()


if __name__ == '__main__':
    decorate(task=2, task_name="tree_height")
