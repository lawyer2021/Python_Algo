# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

number = [random.randint(-100, 100) for i in range(10)]
maximum = max(number)
ind_maximum = number.index(maximum)
minimum = min(number)
ind_minimum = number.index(minimum)
print("Изначальный вариант: ", number)
print(f'Максимальное число: {maximum}, индекс: {ind_maximum}')
print(f'Максимальное число: {min(number)}, индекс: {ind_minimum}')
number.insert(ind_maximum, min(number))
number.pop(ind_maximum + 1)
number.insert(ind_minimum + 1, maximum)
number.pop(ind_minimum)
print("Изменённый вариант: ", number)
print(f'Максимальное число: {maximum}, индекс: {number.index(maximum)}')
print(f'Максимальное число: {min(number)}, индекс: {number.index(min(number))}')
