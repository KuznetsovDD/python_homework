from random import randint
from sys import argv
__all__ = ['guess_number']


def guess_number(low:int=0, up:int=100, counter:int=10)->bool:
    guess = randint(low, up)
    for _ in range(counter):
        number = int(input("Введите число: "))
        if number < guess:
            print("Загаданное число больше")
        elif number > guess:
            print("Загаданное число меньше")
        else:
            print("Поздравляю Вы угадали!")
            return True
    print("Увы, Вы не угадали. Попытки кончились")
    return False

if __name__ == '__main__':
    param = argv[1:]
    guess_number(*(int(item) for item in param))



