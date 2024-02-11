def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Тестирование функции с двумя числами
num1 = 12321
num2 = 12345

# Проверяем, является ли хотя бы одно из чисел палиндромом
result1 = is_palindrome(num1)
result2 = is_palindrome(num2)

print(f"Число {num1} является палиндромом: {result1}")
print(f"Число {num2} является палиндромом: {result2}")
