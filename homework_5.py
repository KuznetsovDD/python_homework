# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def parse_file_path(file_path):
    path, filename = os.path.split(file_path)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension


file_path = "/path/to/file/example.txt"
path, filename, extension = parse_file_path(file_path)
print(parse_file_path(file_path))
print("Путь:", path)
print("Имя файла:", filename)
print("Расширение файла:", extension)

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


names = ["Alice", "Bob", "Charlie"]
rates = [100, 200, 300]
bonuses = ["10.25%", "5.50%", "8.75%"]

result = {name: rate + rate * float(bonus.strip("%")) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

print(result)

# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 10
fibonacci_numbers = list(fibonacci_generator(n))

print(fibonacci_numbers)
