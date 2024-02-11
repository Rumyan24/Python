#include <iostream>
#include <optional>

std::optional<int> piecewise_function(int x) {
    if (x < 0) {
        return std::nullopt;
    } else if (x < 2) {
        return 2;
    } else {
        return 0;
    }
}

int main() {
    int x = 1;
    auto y_calculated = piecewise_function(x);
    if (y_calculated.has_value()) {
        std::cout << "Значение функции при x = " << x << " равно y = " << y_calculated.value() << std::endl;
    } else {
        std::cout << "Функция не определена при x = " << x << std::endl;
    }
    return 0;
}



