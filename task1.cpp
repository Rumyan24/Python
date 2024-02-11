#include <iostream>
#include <cmath>

double calculate_q(double x, double y) {
    return 3 * cos(std::abs(x - 2) - std::abs(y));
}

double calculate_z(double x, double y) {
    double q = calculate_q(x, y);
    double numerator = q + (2 + q) / (std::pow(q, 2) + 3);
    double denominator = 1 / std::sqrt(std::pow(q, 2) + 8);
    return numerator / denominator;
}

int main() {
    std::cout << "Введите значения x и y." << std::endl;
    double x, y;
    std::cout << "x: ";
    std::cin >> x;
    std::cout << "y: ";
    std::cin >> y;
    double z = calculate_z(x, y);
    std::cout << "Результат функции z: " << z << std::endl;
    return 0;
}


