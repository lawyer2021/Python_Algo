# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

numbers = [1]
quantity = int(input("Введите желаемое количество элементов: "))
amount = 0
while quantity > 1:
    numbers.append(numbers[-1] / 2 * -1)
    quantity -= 1
for i in numbers:
    amount += i
print('Ряд заданного количества чисел: ', numbers)
print('Сумма элементов: ', amount)
