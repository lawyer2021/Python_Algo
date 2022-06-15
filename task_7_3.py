# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random

m = int(input("Введите натуральное число m: "))
numbers = [random.randint(0, 50) for _ in range(2 * m + 1)]
# Вариант 1:
print("Массив размером 2m + 1: ", numbers)
print("Медиана массива (вар 1): ", sorted(numbers)[len(numbers) // 2])


# Вариант 2:
def pyramid(nums, heap_size, nums_index):
    big = nums_index
    left_child = (2 * nums_index) + 1
    right_child = (2 * nums_index) + 2
    if left_child < heap_size and nums[left_child] > nums[big]:
        big = left_child
    if right_child < heap_size and nums[right_child] > nums[big]:
        big = right_child
    if big != nums_index:
        nums[nums_index], nums[big] = nums[big], nums[nums_index]
        pyramid(nums, heap_size, big)


def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        pyramid(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        pyramid(nums, i, 0)


heap_sort(numbers)
print("Медиана массива (вар 2): ", numbers[len(numbers) // 2])


# Вариант 3:
def del_max(array):
    array.pop(array.index(max(array)))


def del_min(array):
    array.pop(array.index(min(array)))


while len(numbers) != 1:
    del_max(numbers)
    del_min(numbers)
print("Медиана массива (вар 3): ", numbers[0])
