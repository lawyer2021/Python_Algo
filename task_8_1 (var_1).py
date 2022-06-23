# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# ВАРИАНТ № 1
import random
import string
import hashlib


def generate_random_string(n):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(n))
    print("Строка S длиной", n, ":", rand_string)
    return rand_string


def to_hash(a):
    hash_sub_str = hashlib.sha1(a.encode('utf-8')).hexdigest()
    return hash_sub_str


s = generate_random_string(int(input("Введите длину (N) строки (S): ")))
strings = []
has_bibl = []
sub_str = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] != s]
for i in sub_str:
    h_sub_str = to_hash(i)
    if h_sub_str not in has_bibl:
        strings.append(i)
        has_bibl.append(h_sub_str)
print("Количество различных подстрок в строке S - ", len(strings), ":\n", strings)
