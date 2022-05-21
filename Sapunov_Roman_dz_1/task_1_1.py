# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

from functools import reduce

n = str(input('Введите трехзначное число: '))
all_number = [int(i) for i in n]
multi = reduce(lambda a, b: a * b, all_number)

print('Сумма цифр введенного числа:', sum(all_number))
print('Произведение цифр введенного числа:', multi)
