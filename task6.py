task06.py
# Даны два натуральных числа. Выяснить, является ли хоть одно из них палиндромом, 
# т. е. таким числом, десятичная запись которого читается одинаково слева направо и
# справа налево.
# (Определить функцию, позволяющую распознавать числа-палиндромы до 1010)


# Решение:
#
# Создаем функцию is_palindrome, проверяющую число, является ли оно палиндромом
# как работает функция? мы превращаем наше число в строковый тип,
# переворачиваем строку с помощью среза ([::-1]) и сравниваем
# исходную строку и перевернутую, если они равны, возвращаем True
# а дальше нужно просто вывести текст о том, что одно из чисел палиндром,
# я немножко заморочился с условием и все варианты учёл, но это делать необязательно

def is_palindrome(num):  # создаем функцию
    num = str(num) # превращаем наше число в строковый тип
    return num == num[::-1] # переворачиваем и сравниваем с исходным

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

if is_palindrome(num1) and is_palindrome(num2):
    print('Оба числа - палиндромы')
elif is_palindrome(num1) or is_palindrome(num2):
    print('Одно из чисел - палиндром')
    if is_palindrome(num1):
        print(num1)
    else:
        print(num2)
else:
    print('Палиндромов нет')
