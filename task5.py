import random

original_array = [random.randint(-100, 100) for _ in range(20)]
new_array = [x for x in original_array if x < 0] + [x for x in original_array if x >= 0]

original_array, new_array

print("Исходный массив:")
print(original_array)
print("\nНовый массив сначала с отрицательными числами:")
print(new_array)
