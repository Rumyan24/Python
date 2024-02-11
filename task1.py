import math

# Функция для вычисления q
def calculate_q(x, y):
    return 3 * math.cos(abs(x - 2) - abs(y))

# Функция для вычисления z
def calculate_z(x, y):
    q = calculate_q(x, y)
    numerator = q + (2 + q) / (q**2 + 3)
    denominator = 1 / math.sqrt(q**2 + 8)
    return numerator / denominator

# Теперь мы напишем ту часть программы, которая обрабатывает пользовательский ввод и печатает результат
print("Введите значения x и y.")
x = float(input("x: "))
y = float(input("y: "))

z = calculate_z(x, y)

print(f"Результат функции z: {z}")
