# Значение x задано как 1
x = 1


def piecewise_function(x):
    if x < 0:
        # Функция для этого интервала не определена графиком, возвращаем None
        return None
    elif 0 <= x < 2:
        return 2
    elif x >= 2:
        return 0


# Вычисляем значение y и выводим результат
y_calculated = piecewise_function(x)
print(f"Значение функции при x = {x} равно y = {y_calculated}")
