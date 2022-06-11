# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

# Относительно модуля collections в данной задаче видимо применима deque, но как он может сильно упростить код я не понял.
# 1 ВАРИАНТ:
number_1, number_2 = list(map(str.upper, (input('Введите два шестнадцатеричных числа: ').split())))
numbers_1 = [x for x in ''.join(number_1)]
numbers_2 = [x for x in ''.join(number_2)]
print("Сумма: ", numbers_1, '+', numbers_2, '= ',
      list(map(str.upper, ((hex(int(number_1, 16) + int(number_2, 16)))[2:]))))
print("Произведение: ", numbers_1, '*', numbers_2, '= ',
      list(map(str.upper, ((hex(int(number_1, 16) * int(number_2, 16)))[2:]))))


# 2 ВАРИАНТ:
def table(n):
    for i in range(len(n)):
        if n[i] == 'A':
            n[i] = 10
        elif n[i] == 'B':
            n[i] = 11
        elif n[i] == 'C':
            n[i] = 12
        elif n[i] == 'D':
            n[i] = 13
        elif n[i] == 'E':
            n[i] = 14
        elif n[i] == 'F':
            n[i] = 15
    return n


def to16(s):
    for i in range(len(s)):
        if s[i] == 10:
            s[i] = 'A'
        elif s[i] == 11:
            s[i] = 'B'
        elif s[i] == 12:
            s[i] = 'C'
        elif s[i] == 13:
            s[i] = 'D'
        elif s[i] == 14:
            s[i] = 'E'
        elif s[i] == 15:
            s[i] = 'F'
    return s


def sum16(x, y):
    z = []
    xx = table(x[::-1])
    yy = table(y[::-1])
    if len(xx) >= len(yy):
        for i in range(len(xx) - len(yy)):
            yy.append(0)
    else:
        for i in range(len(yy) - len(xx)):
            xx.append(0)
    p, zz, zzz = 0, 0, 0
    for i in range(len(xx)):
        zz = int(xx[i]) + int(yy[i]) + p
        if zz >= 16:
            p = zz // 16
            zzz = zz % 16
        else:
            zzz = zz
            p = 0
        z.append(zzz)
    if p > 0:
        z.append(p)
    return to16(z[::-1])


def to10(x):
    xx = table(x)
    tenn = 0
    for i in range(len(xx)):
        ll = len(xx) - i - 1
        s = 16 ** ll
        ten = int(xx[i]) * s
        tenn += ten
    return tenn


def mul(x, y):
    x_to_x = x
    for i in range(to10(y) - 1):
        x_to_x = sum16(x, x_to_x)
    return x_to_x


aa = numbers_1
bb = numbers_2
summa = sum16(aa, bb)
print(f"\nСумма чисел {number_1} и {number_2}:")
for i in summa:
    print(i, end="")
dd = mul(aa, bb)
print(f"\nПроизведение чисел {number_1} и {number_2}:")
for i in dd:
    print(i, end="")
