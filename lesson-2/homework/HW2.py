
# 1. Калькулятор возраста
name = input("Введите ваше имя: ")
year_of_birth = int(input("Введите ваш год рождения: "))
current_year = 2025
age = current_year - year_of_birth
print(f"{name}, ваш возраст: {age} лет.")


# 2. Извлечение названия машины
txt = 'LMaasleitbtui'
car_name = txt[1] + txt[3] + txt[5] + txt[7] + txt[9] + txt[11]  # Mercedes (пример скрытого слова)
print("Извлечённое название автомобиля:", car_name)



# 3. Извлечение названия машины
txt = 'MsaatmiazD'
car_name = txt[::2]  # Mazda (если брать через одну букву)
print("Извлечённое название автомобиля:", car_name)


# 4. Извлечение места жительства
txt = "I'am John. I am from London"
city = txt.split("from ")[1]
print("Место жительства:", city)

# 5. Разворот строки
text = input("Введите строку: ")
reversed_text = text[::-1]
print("Строка в обратном порядке:", reversed_text)

# 6. Подсчёт гласных
text = input("Введите строку: ").lower()
vowels = "aeiouаеёиоуыэюя"
count = sum(1 for c in text if c in vowels)
print("Количество гласных букв:", count)

# 7. Нахождение максимального значения
numbers = list(map(int, input("Введите числа через пробел: ").split()))
print("Максимальное значение:", max(numbers))

# 8. Проверка палиндрома
word = input("Введите слово: ").lower()
if word == word[::-1]:
    print("Это палиндром!")
else:
    print("Это не палиндром.")

# 9. Извлечение домена из email
email = input("Введите ваш email: ")
domain = email.split('@')[-1]
print("Домен почты:", domain)

# 10. Генерация случайного пароля
import random
import string

length = int(input("Введите длину пароля: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Случайный пароль:", password)
