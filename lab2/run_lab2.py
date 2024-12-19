from subprocess import *
import unittest
green = '\033[92m'
end = '\033[0m'

def run_tasks():
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')
    files = [
        'task1/src/merge_sort.py',
        'task2/src/merge_sort_plus.py',
        'task3/src/number_of_inversions.py',
        'task4/src/binary_search.py',
        'task9/src/Strassens_method_for_matrix_multiplication.py'
    ]
    for file in files:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests():
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')
    test_files = [
        'task1/tests/test_merge_sort.py',
        'task2/tests/test_merge_sort_plus.py',
        'task3/tests/test_number_of_inversions.py',
        'task4/tests/test_binary_search.py',
        'task9/tests/test_Strassens_method_for_matrix_multiplication.py'
    ]


    for test_file in test_files:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks()
    run_tests()

if __name__ == '__main__':
    main()