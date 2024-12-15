import math
import sys
import os

from lab3.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def nearest_points_to_the_origin(arr_of_points, n, k):
    closest_points = []
    point = 0
    for i in range(k):
        min_dist = 10**9
        for j in range(len(arr_of_points)):
            if math.sqrt((0 - arr_of_points[j][0])**2 + (0 - arr_of_points[j][1])**2) < min_dist:
                min_dist = math.sqrt((0 - arr_of_points[j][0])**2 + (0 - arr_of_points[j][1])**2)
                point = j
        closest_points.append(arr_of_points[point])
        del arr_of_points[point]
    return closest_points


def main():
    input_file = read_input(8)
    n, k = map(int, input_file[0].split())
    arr_of_points = []
    for i in input_file[1:]:
        point = list(map(int, i.split()))
        arr_of_points.append(point)
    res = nearest_points_to_the_origin(arr_of_points, n, k)
    res_string = ''
    for i in res:
        res_string += "," + str(i)
    write_output(8, 'closest points to the origin:', res_string[1:])

if __name__ == '__main__':
    decorate(task = 8, task_name= 'nearest_points_to_the_origin')