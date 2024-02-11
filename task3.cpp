#include <iostream>

int nod(int x, int y) {
    while (x != 0 && y != 0) {
        if (x > y) {
            x = x % y;
        } else {
            y = y % x;
        }
    }
    return x + y;
}

int main() {
    int a, b, c;
    std::cout << "a: ";
    std::cin >> a;
    std::cout << "b: ";
    std::cin >> b;
    std::cout << "c: ";
    std::cin >> c;
    std::cout << "НОД трёх натуральных чисел: " << nod(nod(a, b), c) << std::endl;
    return 0;
}


