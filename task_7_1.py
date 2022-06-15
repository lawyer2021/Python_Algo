# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random
from time import perf_counter


# Вариант 1:
def bubble_sort_1(array):
    for i in range(len(array)):
        for n in range(len(array) - 1):
            if array[n] < array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
    return array


# Вариант 2:
def bubble_sort_2(array):
    flag = True
    while flag:
        flag = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True
    return array


numbers = [random.randint(-100, 100) for _ in range(10)]
print("Исходный массив: ", numbers)
start_1 = perf_counter()
print("Отсортированный массив (вар 1): ", bubble_sort_1(numbers))
stop_1 = perf_counter()
print("Время 1: ", stop_1 - start_1)
start_2 = perf_counter()
print("Отсортированный массив (вар 2): ", bubble_sort_2(numbers))
stop_2 = perf_counter()
print("Время 2: ", stop_2 - start_2)
