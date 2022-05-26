# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

number = [i for i in range(2, 100)]
divider = [i for i in range(2, 10)]
multiplicity = 0
for i in number:
    for d in divider:
        if i % d == 0:
            multiplicity += 1
print(multiplicity, 'чисел диапазона кратны каждому из чисел от 2 до 9')
