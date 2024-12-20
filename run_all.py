from subprocess import *
from lab1.run_lab1 import *
from lab2.run_lab2 import *
from lab3.run_lab3 import *
from lab4.run_lab4 import *
from lab5.run_lab5 import *
green = '\033[92m'
end = '\033[0m'
files = []
test_files = []

[files.append(f'lab1/{i}') for i in files1]
[files.append(f'lab2/{i}') for i in files2]
[files.append(f'lab3/{i}') for i in files3]
[files.append(f'lab4/{i}') for i in files4]
[files.append(f'lab5/{i}') for i in files5]

[test_files.append(f'lab1/{i}') for i in test_files1]
[test_files.append(f'lab2/{i}') for i in test_files2]
[test_files.append(f'lab3/{i}') for i in test_files3]
[test_files.append(f'lab4/{i}') for i in test_files4]
[test_files.append(f'lab5/{i}') for i in test_files5]

def run_tasks(files):
    print('-----------------------------------------------------------------------------------------------------------')
    print('Запуск программ')
    print('-----------------------------------------------------------------------------------------------------------')

    for file in files:
        print(f'результат выполнения файла {green}{file}{end}:')
        run(['python', file])
        print('-----------------------------------------------------------------------------------------------------------')


def run_tests(test_files):
    print('Запуск тестов')
    print('-----------------------------------------------------------------------------------------------------------')

    for test_file in test_files:
        print(f'результат выполнения файла {green}{test_file}{end}:')
        # Запуск тестов с использованием unittest
        result = run(['python', '-m', 'unittest', test_file], capture_output=True, text=True)
        print(result.stdout)  # Выводим результат тестов
        print(result.stderr)  # Выводим ошибки, если есть
        print('-----------------------------------------------------------------------------------------------------------')

def main():
    print(files)
    print(test_files)
    run_tasks(files)
    run_tests(test_files)

if __name__ == '__main__':
    main()