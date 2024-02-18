__all__ = ['csv_to_pickles']

from pathlib import Path
import pickle
import csv


def csv_to_pickles(path: Path) -> None:
    with open(path, 'r', encoding='UTF-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel')
        result = []
        for i, row in enumerate(csv_read):
            if i != 0:
                result.append(dict(zip(headers, row)))
            else:
                headers = row

    print(pickle.dumps(result))


if __name__ == '__main__':
    csv_to_pickles(Path('new_users.csv'))