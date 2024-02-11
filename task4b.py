# Функция для нахождения НОД
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для сокращения дроби
def simplify_fraction(numerator, denominator):
    greatest_common_divisor = gcd(numerator, denominator)
    return numerator // greatest_common_divisor, denominator // greatest_common_divisor

# Ввод значений пользователем
numerator_input = input("Введите числитель: ")
denominator_input = input("Введите знаменатель: ")

# Проверяем, являются ли введенные значения числами
try:
    numerator = int(numerator_input)
    denominator = int(denominator_input)
    
    # Сокращение дроби и вывод результата
    p, q = simplify_fraction(numerator, denominator)
    print(f"Сокращенная дробь: {p}/{q}")
except ValueError:
    print("Пожалуйста, введите числа.")
