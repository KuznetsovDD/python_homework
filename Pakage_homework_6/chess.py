import random

__all__ = ['queens_positions', 'generate_queens', 'check_valid']
def queens_safe(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

def generate_queens():
    queens = []
    while len(queens) < 8:
        queen = (random.randint(1, 8), random.randint(1, 8))
        if queen not in queens:
            queens.append(queen)
    return queens


def check_valid(queens):
    # Проверка, что ферзи не находятся друг на друге
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i] == queens[j]:
                return False
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


if __name__ == '__main__':
    queens_positions = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)]
    if queens_safe(queens_positions):
        print("Ферзи не бьют друг друга.")
    else:
        print("Ферзи бьют друг друга.")

    successful_arrangements = 0
    while successful_arrangements < 4:
        queens_positions = generate_queens()
        if check_valid(queens_positions):
            print(f"Успешная расстановка ферзей: {queens_positions}")
            successful_arrangements += 1



