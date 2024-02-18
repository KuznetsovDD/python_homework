#  Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
#  Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size

def traverse_directory_with_info(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for d in dirs:
            dir_path = os.path.join(root, d)
            results.append({'path': dir_path, 'type': 'directory', 'size': get_size(dir_path)})

        for file in files:
            file_path = os.path.join(root, file)
            results.append({'path': file_path, 'type': 'file', 'size': get_size(file_path)})

    with open('results_with_info.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    with open('results_with_info.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['path', 'type', 'size'])
        for result in results:
            csv_writer.writerow([result['path'], result['type'], result['size']])

    with open('results_with_info.pickle', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

# Пример использования функции
traverse_directory_with_info('/path/to/directory')