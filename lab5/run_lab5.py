from subprocess import *
green = '\033[92m'
end = '\033[0m'

files5 = [
    'task1/src/heap.py',
    'task2/src/tree_height.py',
    'task3/src/network_packet.py',
    'task4/src/heap_builder.py'
]

test_files5 = [
    'task1/tests/test_heap.py',
    'task2/tests/test_tree_height.py',
    'task3/tests/test_network_packet.py',
    'task4/tests/test_heap_builder.py'
]

def run_tasks(files5):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files5:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files5):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files5:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    run_tasks(files5)
    run_tests(test_files5)

if __name__ == '__main__':
    main()