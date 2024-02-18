__all__ = ['convert_to_json']

import json
from pathlib import Path


def convert_to_json(path: Path) -> None:
    data = {}
    with(
        open(path, 'r', encoding='UTF-8') as f_read,
        open(path.stem + '.json', 'w', encoding='UTF-8') as f_write
        ):
        for line in f_read:
            name, number = line.split("|")
            data[name.capitalize()] = float(number)
            json.dump(data, f_write)


if __name__ == '__main__':
    convert_to_json(Path('result.txt'))