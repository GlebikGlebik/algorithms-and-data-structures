from subprocess import *
import unittest
green = '\033[92m'
end = '\033[0m'

def run_tasks():
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')
    files = [
        'task1/src/heap.py',
        'task2/src/tree_height.py',
        'task3/src/network_packet.py',
        'task4/src/heap_builder.py'
    ]
    for file in files:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests():
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')
    test_files = [
        'task1/tests/test_heap.py',
        'task2/tests/test_tree_height.py',
        'task3/tests/test_network_packet.py',
        'task4/tests/test_heap_builder.py'
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