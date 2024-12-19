from subprocess import *
import unittest
green = '\033[92m'
end = '\033[0m'

def run_tasks():
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')
    files = [
        'task1/src/random_quick_sort.py',
        'task3/src/scarecrow_sort.py',
        'task5/src/h_index.py',
        'task8/src/nearest_points_to_the_origin.py',
        'task9/src/nearest_points.py'
    ]
    for file in files:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests():
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')
    test_files = [
        'task1/tests/test_random_quick_sort.py',
        'task3/tests/test_scarecrow_sort.py',
        'task5/tests/test_h-index.py',
        'task8/tests/test_nearest_points_to_the_origin.py',
        'task9/tests/test_nearest_points.py'
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