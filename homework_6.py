from random import randint
from sys import argv

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



def puzzles(puzzle: str, answers: list[str], counter: int = 3) -> int:
    print("Отгадай загадку")
    print(f'{puzzle}')
    for i in range(counter):
        answer = input("Введите ответ: ").lower()
    if answer in answers:
        print("Поздравляем, Вы угадали")
    return i + 1
    print("К сожалению Вы не угадали. Попытки исчерпаны.")
    return 0

if __name__ == '__main__':
    puzzles("Зимой и летом одним цветом", ["ель", "елка", "ёлка", "сосна"])