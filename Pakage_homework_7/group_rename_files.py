# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

__all__ = ['group_rename_files']
import os


def group_rename_files(target_name, digits, source_ext, target_ext, name_range=None):
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(source_ext)]

    counter = 1
    for file in files:
        if name_range:
            original_name = file[name_range[0] - 1:name_range[1]]
        else:
            original_name = os.path.splitext(file)[0]

        new_name = f"{original_name}_{target_name}{counter:0{digits}d}.{target_ext}"
        os.rename(file, new_name)
        counter += 1


# Пример использования функции
group_rename_files("newfile", 3, ".txt", "txt", [3, 6])
