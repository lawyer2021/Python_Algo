# 4. Определить, какое число в массиве встречается чаще всего.
import random

number = [random.randint(0, 10) for i in range(25)]
print(number)
maximum = 0
for i in number:
    if number.count(i) > maximum:
        num = i
        maximum = number.count(i)
print(f'Число {num} встречается {number.count(num)} раз(а)')
