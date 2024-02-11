def rearrange_array(arr):
    # Инициализация указателя
    j = 0
    for i in range(len(arr)):
        # Если текущий элемент отрицателен, меняем его местами с элементом на позиции указателя
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

# Пример массива
example_arr = [-1, 3, -5, 2, 4, -6, 7, -2]

# Перераспределение массива
rearranged_arr = rearrange_array(example_arr)
print(rearranged_arr)
