# '''
# 2. Напишите программу, которая получает целое число и возвращает его
#  шестнадцатеричное строковое представление. Функцию hex используйте
#  для проверки своего результата.
# '''
# num = int(input("Введите целое число: "))
# hex_num = ""
# HEX_DIGITS = "0123456789ABCDEF"
#
# if num == 0:
#     hex_num = "0"
# else:
#     while num > 0:
#         remainder = num % 16
#         hex_num = HEX_DIGITS[remainder] + hex_num
#         num = num // 16
#
# hex_num_2 = hex(num)
#
#
# print(f"Шестнадцатеричное представление числа: {hex_num}")
#
# print(f"Шестнадцатеричное представление числа: {hex_num_2}")


'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions

'''

from fractions import Fraction

def get_fraction_from_input():
    input_str = input("Введите дробь в формате a/b: ")
    parts = input_str.split('/')
    if len(parts) != 2:
        raise ValueError("Неверный формат дроби")
    numerator = int(parts[0])
    denominator = int(parts[1])
    return (numerator, denominator)

def get_fraction(input_function):
    numerator, denominator = input_function
    return Fraction(numerator, denominator)

def add_fractions(fraction1, fraction2):
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2
    common_denominator = denominator1 * denominator2
    new_numerator1 = numerator1 * denominator2
    new_numerator2 = numerator2 * denominator1
    new_numerator_sum = new_numerator1 + new_numerator2
    return (new_numerator_sum, common_denominator)

def multiply_fractions(fraction1, fraction2):
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2
    new_numerator = numerator1 * numerator2
    new_denominator = denominator1 * denominator2
    for i in range(1, new_numerator):
        if new_numerator % i == 0 and new_denominator % i == 0:
            new_denominator = int(new_denominator / i)
            new_numerator = int(new_numerator / i)

    return (new_numerator, new_denominator)


fraction1 = get_fraction_from_input()
fraction2 = get_fraction_from_input()

fraction_1 = get_fraction(fraction1)
fraction_2 = get_fraction(fraction2)

sum_fraction = add_fractions(fraction1, fraction2)
product_fraction = multiply_fractions(fraction1, fraction2)

sum_fraction_1 = fraction_1 + fraction_2
product_fraction_2 = fraction_1 * fraction_2

print(f"Сумма дробей: {sum_fraction[0]}/{sum_fraction[1]}")
print(f"Произведение дробей: {product_fraction[0]}/{product_fraction[1]}")

print(f"Сумма дробей: {sum_fraction_1}")
print(f"Произведение дробей: {product_fraction_2}")









