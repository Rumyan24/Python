#include <iostream>
#include <string>
#include <algorithm>

// Функция для проверки, является ли число палиндромом
bool is_palindrome(int number) {
    std::string original = std::to_string(number);
    std::string reversed = original;
    std::reverse(reversed.begin(), reversed.end());
    return original == reversed;
}

int main() {
    int num1 = 12321; // Пример числа
    int num2 = 12345; // Пример числа

    // Проверяем, является ли хотя бы одно из чисел палиндромом
    bool result1 = is_palindrome(num1);
    bool result2 = is_palindrome(num2);

    std::cout << "Число " << num1 << " является палиндромом: " << result1 << std::endl;
    std::cout << "Число " << num2 << " является палиндромом: " << result2 << std::endl;

    return 0;
}
