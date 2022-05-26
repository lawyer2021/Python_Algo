# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

numbers = [random.randint(-10, 10) for i in range(1, 10)]
print("Массив: ", numbers)
print("Два наименьших элемента: ", min(numbers),
      min(numbers[:numbers.index(min(numbers))] + numbers[numbers.index(min(numbers)) + 1:]))
# ИЛИ:
print("Минимум 1: ", min(numbers))
numbers.pop(numbers.index(min(numbers)))
print("Минимум 2: ", min(numbers))