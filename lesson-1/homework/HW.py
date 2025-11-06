# 1) Дана сторона квадрата. Найти периметр и площадь.
a = float(input("Введите сторону квадрата a: "))
perimeter_square = 4 * a
area_square = a ** 2
print(f"\nПериметр квадрата = {perimeter_square}")
print(f"Площадь квадрата = {area_square}")

# 2) Дан диаметр окружности. Найти её длину.
d = float(input("\nВведите диаметр окружности d: "))
length_circle = math.pi * d
print(f"Длина окружности = {length_circle}")

# 3) Даны два числа a и b. Найти их среднее арифметическое.
a = float(input("\nВведите число a: "))
b = float(input("Введите число b: "))
mean = (a + b) / 2
print(f"Среднее арифметическое чисел {a} и {b} = {mean}")

# 4) Даны два числа a и b. Найти их сумму, произведение и квадрат каждого числа.
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2
print(f"\nСумма чисел = {sum_ab}")
print(f"Произведение чисел = {product_ab}")
print(f"Квадрат числа a = {square_a}")
print(f"Квадрат числа b = {square_b}")
