#include <iostream>
#include <string>
#include <algorithm>

// Функция для проверки, является ли число палиндромом
bool is_palindrome(int num) {
    std::string str = std::to_string(num);
    std::string reversed_str = str;
    std::reverse(reversed_str.begin(), reversed_str.end());
    return str == reversed_str;
}

int main() {
    int num1, num2;

    std::cout << "Введите первое число: ";
    std::cin >> num1;

    std::cout << "Введите второе число: ";
    std::cin >> num2;

    if (is_palindrome(num1) && is_palindrome(num2)) {
        std::cout << "Оба числа - палиндромы" << std::endl;
    } else if (is_palindrome(num1) || is_palindrome(num2)) {
        std::cout << "Одно из чисел - палиндром" << std::endl;
        if (is_palindrome(num1)) {
            std::cout << num1 << std::endl;
        } else {
            std::cout << num2 << std::endl;
        }
    } else {
        std::cout << "Палиндромов нет" << std::endl;
    }

    return 0;
}
