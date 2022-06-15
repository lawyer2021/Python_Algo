# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

# 64 битная система
# Version Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18)
import random
from collections.abc import Mapping, Container
from sys import getsizeof


def deep_getsizeof(o, ids):
    d = deep_getsizeof
    if id(o) in ids:
        return 0
    r = getsizeof(o)
    ids.add(id(o))
    if isinstance(o, str) or isinstance(0, str):
        return r
    if isinstance(o, Mapping):
        return r + sum(d(k, ids) + d(v, ids) for k, v in o.iteritems())
    if isinstance(o, Container):
        return r + sum(d(x, ids) for x in o)
    return r


# Задача № 1
# Вариант 1
number1 = [random.randint(-100, 100) for _ in range(5)]
maximum = max(number1)
ind_maximum = number1.index(maximum)
minimum = min(number1)
ind_minimum = number1.index(minimum)
print("Изначальный вариант: ", number1)
number1.insert(ind_maximum, min(number1))
number1.pop(ind_maximum + 1)
number1.insert(ind_minimum + 1, maximum)
number1.pop(ind_minimum)
print("Изменённый вариант: ", number1)
print('Размер списка number1: ', deep_getsizeof(number1, set()))  # 56 + 5*8 + 5*28
print('Размеры переменных maximum, ind_maximum, minimum, ind_minimum: ', (deep_getsizeof(maximum, set())),
      (deep_getsizeof(ind_maximum, set())), (deep_getsizeof(minimum, set())), (deep_getsizeof(ind_minimum, set())),
      '\n')  # 28, 28, 28, 28
# При оптимизации по памяти можно значения максимума и минимума не сохранять в отдельные переменные, а использовать
# сразу при присвоении. Тогда объем занимаемой памяти уменьшится на количесвто двух переменных, состоящих из чисел,
# т.е. 28 + 28 = 56
# Задача № 1
# Вариант 2
number2 = [random.randint(-100, 100) for _ in range(5)]
print("Изначальный вариант: ", number2)
ind_maximum_2 = number2.index(max(number2))
ind_minimum_2 = number2.index(min(number2))
number2[ind_minimum_2], number2[ind_maximum_2] = number2[ind_maximum_2], number2[ind_minimum_2]
print("Изменённый вариант: ", number2)
print('Размер списка number2: ', deep_getsizeof(number2, set()))  # 56 + 5*8 + 5*28
print('Размеры переменных ind_maximum_2, ind_minimum_2: ', (deep_getsizeof(ind_maximum_2, set())),
      (deep_getsizeof(ind_minimum_2, set())), '\n')  # 28, 28
# Задача № 2
# Вариант 1
number = '94675'
even = []
counts_even = 0
odd = []
counts_odd = 0
for i in range(len(number)):
    if int(number[i]) % 2:
        odd.append(number[i])
        counts_odd += 1
    else:
        even.append(number[i])
        counts_even += 1
print(f'Четных цифр: {counts_even} ({",".join(even)}), нечетных цифр: {counts_odd} ({",".join(odd)})')
print('Размер пустой строки', deep_getsizeof('', set()))
print('Размер введенного числа', deep_getsizeof(number, set()))
print('Список четных чисел', even)
print('Размер списка четных чисел', deep_getsizeof(even, set()))
print('Список нечетных чисел', odd)
print('Размер списка нечетных чисел', deep_getsizeof(odd, set()), '\n')
# Пустая строка занимает 49
# Строковая переменная number состоит из 5 символов и занимает 5 * 1 = 5
# Итого number это 54 байта (49 + 5)

# Пустой список занимает 56
# Пустая строка занимает 49
# 1 строковый символ занимает 1
# В переменную even попало 2 строковых значения: 49 * 2 + 2 * 1 = 100
# 2 ссылки по 8 = 16
# Итого even это 172 байта (56 + 100 + 16)

# Пустой список занимает 56
# Пустая строка занимает 49
# 1 строковый символ занимает 1
# в переменную odd  попало 3 строковых значения: 49 * 3 + 3 * 1 = 150
# 3 ссылки по 8 = 24
# Итого odd это 230 байта (56 + 150 + 24)

# Переменные counts_even и counts_odd это числа по 28 байт каждое.

# При оптимизации по памяти можно значения, заносимые в списки odd и even, привести к int.
# Тогда объем занимаемой памяти уменьшится, т.к. списки будут состоять не из строковых значений, а из чисел

# Задача № 2
# Вариант 2
even = []
counts_even = 0
odd = []
counts_odd = 0
for i in range(len(number)):
    if int(number[i]) % 2:
        odd.append(int(number[i]))
        counts_odd += 1
    else:
        even.append(int(number[i]))
        counts_even += 1
print(f'Четных цифр: {counts_even} ({even}), нечетных цифр: {counts_odd} ({odd})')
print('Список четных чисел', even)
print('Размер списка нечетных чисел', deep_getsizeof(even, set()))
print('Список нечетных чисел', odd)
print('Размер списка нечетных чисел', deep_getsizeof(odd, set()))
