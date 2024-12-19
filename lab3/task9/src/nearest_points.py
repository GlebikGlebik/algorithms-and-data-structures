import sys
import os
import math

from lab3.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def nearest_point(arr_of_points, n):
    min_dist = 10**9
    index1 = 0
    index2 = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if math.sqrt((arr_of_points[i][0] - arr_of_points[j][0])**2 + (arr_of_points[i][1] - arr_of_points[j][1])**2) < min_dist:
                min_dist = math.sqrt((arr_of_points[i][0] - arr_of_points[j][0])**2 + (arr_of_points[i][1] - arr_of_points[j][1])**2)
                index1 = i
                index2 = j
    indexes = (index1, index2)
    return indexes, min_dist


def main():
    input_file = read_input(9)
    n = int(input_file[0])
    arr_of_points = {}
    key = 0
    for i in input_file[1:]:
        point = tuple(map(int, i.split()))
        arr_of_points[key] = point
        key += 1
    res, min_dist = nearest_point(arr_of_points, n)

    write_output(9, str(min_dist))

if __name__ == '__main__':
    decorate(task = 9, task_name= 'nearest_points')