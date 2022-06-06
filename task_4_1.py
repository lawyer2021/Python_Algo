# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import random
from time import perf_counter


numbers = [random.randint(-10, 10) for i in range(1, 100000)]

start = perf_counter()
# print("Массив: ", numbers)
print("Два наименьших элемента: ", min(numbers),
      min(numbers[:numbers.index(min(numbers))] + numbers[numbers.index(min(numbers)) + 1:]))
print("time 1: ", perf_counter() - start)

# ИЛИ:
start1 = perf_counter()
print("Минимум 1: ", min(numbers))
numbers.pop(numbers.index(min(numbers)))
print("Минимум 2: ", min(numbers))

print("time 2: ", perf_counter() - start1)


# Скорость выполнения второго варианта алгоритма почти в 10 раз меньше первого
# Сложность обоих алготритмов линейная. Но сложность первого алгоритма представляется выше, т.к. используется 4 вызова функции MIN, срез и определение индексов у двух значений.
# Во втором алгоритме функция MIN вызывается три раза, одно определение индекса и функция POP
