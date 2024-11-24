from math import degrees


def strassen_multiplication(a, b, n):
    """
    :param a: 1 матрица
    :param b: 2 матрица
    :param n: их квадратный порядок
    :return: произведение матриц 1 и 2
    """
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    mid = n // 2

    a11 = [row[:mid] for row in a[:mid]]
    a12 = [row[mid:] for row in a[:mid]]
    a21 = [row[:mid] for row in a[mid:]]
    a22 = [row[mid:] for row in a[mid:]]

    b11 = [row[:mid] for row in b[:mid]]
    b12 = [row[mid:] for row in b[:mid]]
    b21 = [row[:mid] for row in b[mid:]]
    b22 = [row[mid:] for row in b[mid:]]

    m1 = strassen_multiplication(matrix_sum(a11, a22), matrix_sum(b11, b22), mid)
    m2 = strassen_multiplication(matrix_sum(a21, a22), b11, mid)
    m3 = strassen_multiplication(a11, matrix_minus(b12, b22), mid)
    m4 = strassen_multiplication(a22, matrix_minus(b21, b11), mid)
    m5 = strassen_multiplication(matrix_sum(a11, a12), b22, mid)
    m6 = strassen_multiplication(matrix_minus(a21, a11), matrix_sum(b11, b12), mid)
    m7 = strassen_multiplication(matrix_minus(a12, a22), matrix_sum(b21, b22), mid)

    c11 = matrix_sum(matrix_minus(matrix_sum(m1, m4), m5), m7)
    c12 = matrix_sum(m3, m5)
    c21 = matrix_sum(m2, m4)
    c22 = matrix_sum(matrix_minus(matrix_sum(m1, m3), m2), m6)

    new_matrix = []
    for i in range(mid):
        new_matrix.append(c11[i] + c12[i])
    for i in range(mid):
        new_matrix.append(c21[i] + c22[i])

    return new_matrix

def matrix_maker(a, n):
    matrix = []
    for i in range(0, len(a), n):
        matrix.append(a[i: i + n])
    return matrix

def matrix_sum(a, b):
    """Сложение матриц"""
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrix_minus(a, b):
    """Вычитание матриц"""
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def pad_matrix(matrix, new_size):
    padded = [[0] * new_size for _ in range(new_size)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            padded[i][j] = matrix[i][j]
    return padded

a_input = input().split()
b_input = input().split()
n = int(input())
degrees_of_two = set()
[degrees_of_two.add(2**x) for x in range(10)]
if n not in degrees_of_two:
    a = matrix_maker(list(map(int, a_input)), n)
    b = matrix_maker(list(map(int, b_input)), n)

result = strassen_multiplication(a, b, n)

for row in result:
    print(" ".join(map(str, row)))