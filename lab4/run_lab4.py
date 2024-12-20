from subprocess import *
green = '\033[92m'
end = '\033[0m'

files4 = [
    'task1/src/stack.py',
    'task2/src/queue.py',
    'task3/src/bracket_sequence_1.py',
    'task5/src/stack_with_max.py',
    'task7/src/max_in_moving_sequence.py'
]

test_files4 = [
    'task1/tests/test_stack.py',
    'task2/tests/test_queue.py',
    'task3/tests/test_bracket_sequence_1.py',
    'task5/tests/test_stack_with_max.py',
    'task7/tests/test_max_in_moving_sequence.py'
]

def run_tasks(files4):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files4:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files4):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files4:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files4)
    run_tests(test_files4)

if __name__ == '__main__':
    main()