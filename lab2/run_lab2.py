from subprocess import *
green = '\033[92m'
end = '\033[0m'

files2 = [
    'task1/src/merge_sort.py',
    'task2/src/merge_sort_plus.py',
    'task3/src/number_of_inversions.py',
    'task4/src/binary_search.py',
    'task9/src/Strassens_method_for_matrix_multiplication.py'
]

test_files2 = [
    'task1/tests/test_merge_sort.py',
    'task2/tests/test_merge_sort_plus.py',
    'task3/tests/test_number_of_inversions.py',
    'task4/tests/test_binary_search.py',
    'task9/tests/test_Strassens_method_for_matrix_multiplication.py'
]

def run_tasks(files2):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files2:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files2):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files2:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files2)
    run_tests(test_files2)

if __name__ == '__main__':
    main()