# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = input("Введите число: ")
even = []
counts_even = 0
odd = []
counts_odd = 0
for i in range(len(number)):
    if int(number[i]) % 2:
        even.append(number[i])
        counts_even += 1
    else:
        odd.append(number[i])
        counts_odd += 1
print(f'Четных цифр: {counts_even} ({",".join(even)}), нечетных цифр: {counts_odd} ({",".join(odd)})')
