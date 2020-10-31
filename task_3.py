"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib


def lines(a):
    my_list = list(a)
    c = set()
    for i in range(len(my_list)):
        for j in range(len(my_list)-1 if i == 0 else len(my_list), i, -1):
            c.add(hashlib.sha3_256((''.join(my_list[i:j]).encode())).hexdigest())
            # c.add((''.join(my_list[i:j])))
    return len(c)


my_str = 'papa'
print(lines(my_str))

