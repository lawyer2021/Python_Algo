# 9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = map(int, (input('Введите три числа: ').split()))
if a == b:
    raise Exception('Ошибка, введены два одинаковых числа - первое и второе')
elif a == c:
    raise Exception('Ошибка, введены два одинаковых числа - первое и третье')
elif b == c:
    raise Exception('Ошибка, введены два одинаковых числа - третье и второе')

if a > b:
    if a < c:
        print('Среднее первое: ', a)
    elif b > c:
        print('Среднее второе: ', b)
    else:
        print('Среднее третье: ', c)
elif b < c:
    print('Среднее второе: ', b)
else:
    print('Среднее третье: ', c)
