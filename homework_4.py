# Напишите функцию для транспонирования матрицы

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose_matrix(matrix):

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed = [[matrix[j][i] for j in range(num_rows)] for i in range(num_cols)]

    return transposed

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def create_dict(**kwargs):
    result_dict = {}

    for key, value in kwargs.items():
        if isinstance(key, (int, float, complex)):
            key = str(key)
        result_dict[value] = key

    return result_dict



result = create_dict(a=1, b='hello', c=3.14)
print(result)


# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal

decimal.getcontext().prec = 2
MULTIPLICITY = 50
PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_PERC = 3
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = "1"
CMD_WITHDRAW = "2"
CMD_EXIT = "3"

balance = 0
operations = 0
transactions = []


def deposit(amount):
    global balance, operations
    operations += 1
    balance += amount
    transactions.append(f"Пополнение: +{amount}")


def withdraw(amount):
    global balance, operations
    comission = amount * PERCENT
    comission = max(MIN_LIMIT, min(comission, MAX_LIMIT))
    if comission + amount > balance:
        print("На балансе недостаточно средств")
        return
    operations += 1
    balance -= (amount + comission)
    transactions.append(f"Снятие: -{amount} (комиссия {comission})")


def apply_bonus():
    global balance
    bonus_sum = balance * PERCENT_BONUS
    balance += bonus_sum
    transactions.append(f"Бонус: +{bonus_sum}")


while True:
    action = input(
        f"пополнить-{CMD_DEPOSIT}\n"
        f"снять-{CMD_WITHDRAW}\n"
        f"выход-{CMD_EXIT}\n"
        f"Введите действие: "
    )

    if balance > RICHNESS_AMOUNT and action != CMD_EXIT:
        sum_percent = balance * PERCENT_RICHNESS
        balance -= sum_percent
        print(f"Вычтен налог на богатство в размере {sum_percent}")
        print(f"Текущий баланс {balance}")

    if action == CMD_DEPOSIT or action == CMD_WITHDRAW:
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))

        if action == CMD_DEPOSIT:
            deposit(amount)
        else:
            withdraw(amount)

        if operations % COUNT_PERC == 0:
            apply_bonus()

        print(f"Текущий баланс {balance}")

    elif action == CMD_EXIT:
        break

    else:
        print("Введена неверная команда")

print("Операции:")
for transaction in transactions:
    print(transaction)

