_data = {}

__all__ = ['puzzles', 'puzzles_storage']


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


def puzzles_storage():
    storage = {
    "Зимой и летом одним цветом": ["ель", "елка", "ёлка", "сосна"],
    "Не лает, не кусает, в дом не пускает": ["замок", "засов", "домофон"],
    "Висит груша, нельзя скушать": ["лампа", "лампочка", "светильник"]
    }
    for k, v in storage.items():
        result = puzzles(k, v)
        save_results(k, result)
    print("Не угадал" if not result else f"Вы угадали с {result} попытки")


def save_results(text: str, num: int):
    _data[text] = num


def show_results():
    res = (
        f"Загадку {k} не угадали" if not v
        else f"Вы угадали загадку {k} с {v} попытки"
        for k, v in _data.items()
    )
    print(*res, sep='\n')


if __name__ == '__main__':
    puzzles_storage()
    show_results()