# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

import random

number = [random.randint(10, 1000) for i in range(10)]
amount, maximum, max_number = (0,) * 3
for i in number:
    for n in str(i):
        amount += int(n)
        if amount > maximum:
            maximum = amount
            max_number = i
    amount = 0
print('Введенные числа: ', number)
print(f'Наибольшее число по сумме цифр: {max_number} (с суммой цифр: {maximum})')
