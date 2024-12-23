from subprocess import *
green = '\033[92m'
end = '\033[0m'

files6 = [
    'task1/src/array.py',
    'task2/src/phone_book.py',
    'task4/src/associative_array.py',
]

test_files6 = [
    'task1/tests/test_array.py',
    'task2/tests/test_phone_book.py',
    'task4/tests/test_associative_array.py',
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
    run_tasks(files6)
    run_tests(test_files6)

if __name__ == '__main__':
    main()