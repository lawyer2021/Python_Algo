# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random
import operator

numbers = [random.randint(0, 50) for _ in range(10)]


def merge_sort(array, compare=operator.lt):
    if len(array) < 2:
        return array[:]
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle], compare)
        right = merge_sort(array[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, n = 0, 0
    while i < len(left) and n < len(right):
        if compare(left[i], right[n]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[n])
            n += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while n < len(right):
        result.append(right[n])
        n += 1
    return result


print("Исходный массив: ", numbers)
print("Отсортированный массив: ", merge_sort(numbers))
