import math

def calculate_a(e, f ,g):
    return (math.exp(-1/f) / g)**(1/4) + g

def calculate_b(e, h):
    return math.sin(e) + math.cos(h)**4

def calculate_c(e, f, g):
    if e * f - 4 == 0:
        raise ValueError("Знаменатель не может быть равен нулю при расчете с.")
    
    return 44*g / (e * f - 4)
    
# Ввод значений пользователем
e = float(input("Введите значение для e:"))
f = float(input("Введите значение для f:"))
g = float(input("Введите значение для g:"))
h = float(input("Введите значение для h:"))
    
# предположим что h такое же как g

    
a = calculate_a(e, f, g)
b = calculate_a(e, h, g)
c = calculate_a(e, f, g)
    
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
