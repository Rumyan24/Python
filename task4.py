def is_member_of_arithmetic_sequence(n ,F,s):
    
    return (n - F) % s == 0

F = float(input("Введите первый член прогрессии F:"))
s = float(input("Введите шаг прогрессии s: "))
n = float(input("Введите проверяемое число n:"))

if is_member_of_arithmetic_sequence(n ,F,s):
    print(f"Число {n}  является членом арифметической прогресии.")
else:
    print(f"Число {n} не является членом арифметической прогресии.")
