# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов


input_list = [1, 2, 2, 3, 4, 4, 5]
result_list = set()
for item in input_list:
    count = 0
    for i in input_list:
        if i == item:
            count += 1
    if count > 1:
        result_list.add(item)

print(list(result_list))

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

from collections import Counter
FREQENTLY_OCCURING_WORDS = 10


text = """
    Python is an easy to learn, powerful programming language. 
    It has efficient high-level data structures and a simple 
    but effective approach to object-oriented programming. 
    Python’s elegant syntax and dynamic typing, together with its interpreted nature, 
    make it an ideal language for scripting and rapid application development in many areas on most platforms.
    
    The Python interpreter and the extensive 
    standard library are freely available in source or binary form for all 
    major platforms from the Python web site, https://www.python.org/, and may be freely distributed. 
    The same site also contains distributions of and pointers to many free third party Python modules, 
    programs and tools, and additional documentation.
    
    The Python interpreter is easily extended with new functions and data types implemented in C or C++ 
    (or other languages callable from C). Python is also suitable as an extension language 
    for customizable applications.
    
    This tutorial introduces the reader informally to the basic concepts and features of the Python 
    language and system. It helps to have a Python interpreter handy for hands-on experience, but all 
    examples are self-contained, so the tutorial can be read off-line as well.
"""



final_text = text.replace(",", "").replace(".", "").lower()

words = final_text.split()
word_counts = Counter(words)
print(word_counts.most_common(10))


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

items = {
    'спальник': 3,
    'еда': 2,
    'вода': 1,
    'топор': 1,
    'фонарик': 1,
    'палатка': 4
}
MAX_WEIGHT = 7
backpack_contents = []
current_weight = 0
for item, weight in items.items():
    if current_weight + weight <= MAX_WEIGHT:
        backpack_contents.append(item)
        current_weight += weight
print(backpack_contents)







