#include <iostream>
#include <vector>
#include <cstdlib> // For rand() and srand()
#include <ctime> // For time()

int main() {
    srand(static_cast<unsigned int>(time(0))); // Seed the random number generator

    std::vector<int> arr;
    for (int i = 0; i < 10; ++i) {
        arr.push_back(rand() % 21 - 10); // Random number between -10 and 10
    }

    std::vector<int> neg_arr;
    std::vector<int> pos_arr;

    for (int num : arr) {
        if (num < 0) {
            neg_arr.push_back(num);
        } else {
            pos_arr.push_back(num);
        }
    }

    std::cout << "Исходный массив: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::cout << "Новый массив: ";
    for (int num : neg_arr) {
        std::cout << num << " ";
    }
    for (int num : pos_arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}


