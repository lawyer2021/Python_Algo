# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

start = -100
number = [random.randint(start, 10) for i in range(25)]
for i in number:
    if i < 0:
        if i > start:
            start = i
print(number)
print(f'Максимальный отрицательный элемент: {start} на позиции: {number.index(start)}')
