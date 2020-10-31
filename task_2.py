"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib

def hash():
    for k, v in users.items():
        res = hashlib.sha3_256(k.encode()+v.encode()).hexdigest()
        pass_hash.append(res)
    return pass_hash

def authentication():
    a = input("Enter your name: ")
    b = input("Enter your password: ")

    res = hashlib.sha3_256(a.encode() + b.encode()).hexdigest()
    for i in pass_hash:
        if i == res:
            c = input("Enter your password again: ")
            res_2 = hashlib.sha3_256(a.encode() + c.encode()).hexdigest()
            if res_2 == res:
                print("Вы ввели правильный пароль!")
                break
        else:
            print("Вы ввели неправильный пароль!")
            break



users = {"Konstantin": "111111","Julia": "222222","Ivan": "333333"}
pass_hash = []
print(hash())
authentication()