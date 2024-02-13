# # a = 10
# # b = 12
# # c = 10
# #
# #
# #
# # if  b + c < a or c + a < b or a + b < c:
# #     print("Not triangle")
# # else:
# #     print("Triangle")
# #     if a == b and a != c or b == c and b != a or c == a and a != b:
# #         print("Равноберенный")
# #     elif a == b and a == c:
# #         print("Равносторонний")
# #     else:
# #         print("Разносторонний")
# #
# #
# MAX_NUM = 100000
# MIN_NUM = 0
# TWO = 2
#
#
# num = int(input("Введите число: "))
#
# if num < MAX_NUM and num > MIN_NUM:
#     count = 0
#
#     for i in range(num):
#         if num % (i + 1) == 0:
#             count += 1
#     if count > TWO:
#         print("Составное число")
#     else:
#         print("Простое число")
# else:
#     print("Неверный диапазон")

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT = 10


from random import randint
a = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 0
for i in range(COUNT):
    count += 1
    num = int(input("Введите число: "))
    print(f"Попытка {count}")

    if a > num:
        print("Больше")

    elif a < num:
        print("Меньше")
    elif a == num:
        print("Верно")
        break

print("Конец игры")
print(f"Количество попыток {count}")