# 7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a, b, c = map(int, (input('Введите длины трех отрезков через пробел : ').split()))
if ((a + b) > c) & ((a + c) > b) & ((b + c) > a):
    print('Из указанных отрезков можно составить треугольник')
    if (a == b) | (a == c) | (b == c):
        if a == b == c:
            print('Полученнный треугольник равносторонний')
        else:
            print('Полученнный треугольник равнобедренный')
    else:
        print('Полученнный треугольник разносторонний')
else:
    print("Из указанных отрезков нельзя составить треугольник")
