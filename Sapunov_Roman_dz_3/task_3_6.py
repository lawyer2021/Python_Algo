# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

numbers = [random.randint(1, 100) for i in range(1, 50, 7)]
print('Элементы: ', numbers)
if numbers.index(max(numbers)) > numbers.index(min(numbers)):
    print(sum(numbers[numbers.index(min(numbers)) + 1:numbers.index(max(numbers))]))
else:
    print('Сумма элементов, находящихся между минимальным и максимальным элементами: ',
          sum(numbers[numbers.index(max(numbers)) + 1:numbers.index(min(numbers))]))
