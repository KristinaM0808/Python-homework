# 1. Сортировка словаря по значениям
my_dict = {'a': 3, 'b': 1, 'c': 2}

# По возрастанию
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# По убыванию
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Сортировка по возрастанию:", ascending)
print("Сортировка по убыванию:", descending)

# 2. Добавление нового ключа в словарь
d = {0: 10, 1: 20}
d[2] = 30
print("Обновлённый словарь:", d)

# 3. Конкатенация нескольких словарей
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {}
for d in (dic1, dic2, dic3):
    merged_dict.update(d)

print("Объединённый словарь:", merged_dict)


# 4. Генерация словаря квадратов чисел
n = int(input("Введите число n: "))
squares = {x: x**2 for x in range(1, n+1)}
print("Словарь квадратов:", squares)


# 5. Словарь квадратов от 1 до 15
squares_15 = {x: x**2 for x in range(1, 16)}
print("Словарь квадратов (1–15):", squares_15)

# Set Exercises
# 1. Создание множества
my_set = {"яблоко", "банан", "киви"}
print("Созданное множество:", my_set)

# 2. Перебор элементов множества
fruits = {"яблоко", "банан", "груша"}
print("Элементы множества:")
for fruit in fruits:
    print(fruit)

# 3. Добавление элементов
numbers = {1, 2, 3}
numbers.add(4)
numbers.update([5, 6])
print("После добавления:", numbers)

# 4. Удаление элемента
colors = {"red", "blue", "green"}
colors.remove("blue")  # выдаст ошибку, если элемента нет
print("После удаления:", colors)

# 5. Безопасное удаление (если элемент существует)
cities = {"London", "Paris", "Rome"}
cities.discard("Paris")  # не выдаст ошибку, если элемента нет
print("После удаления (если был):", cities)
