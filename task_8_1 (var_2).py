# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# ВАРИАНТ № 2
import random
import string
import hashlib


def generate_random_string(n):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(n))
    print("Строка S длиной", n, ":", rand_string)
    return rand_string


s = generate_random_string(int(input("Введите длину (N) строки (S): ")))
strings_var2 = {}
sub_str = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] != s]
for i in sub_str:
    strings_var2[hashlib.sha1(i.encode('utf-8')).hexdigest()] = i
print("Количество различных подстрок в строке S - ", len(strings_var2), ":\n", strings_var2)
