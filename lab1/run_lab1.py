from subprocess import *
green = '\033[92m'
end = '\033[0m'

files1 = [
    'task1/src/task1.py',
    'task3/src/task3_recursive_insertion_sort.py',
    'task4/src/task4.py',
    'task5/src/task5.py',
    'task6/src/task6.py',
    'task7/src/task7.py',
    'task8/src/task8.py'
]

test_files1 = [
    'task1/tests/test_task1.py',
    'task3/tests/test_task3_recursive_insertion_sort.py',
    'task4/tests/test_task4.py',
    'task5/tests/test_task5.py',
    'task6/tests/test_task6.py',
    'task7/tests/test_task7.py',
    'task8/tests/test_task8.py'
]

def run_tasks(files1):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files1:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files1):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files1:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files1)
    run_tests(test_files1)

if __name__ == '__main__':
    main()