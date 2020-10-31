"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

# def cache(a):
#     salt = 'any_salt'
#     res = hashlib.sha3_256(a.encode() + salt.encode()).hexdigest()
#     my_cache.append(res)
#     return my_cache
#
# def check_cache(a):
#     salt = 'any_salt'
#     res = hashlib.sha3_256(a.encode() + salt.encode()).hexdigest()
#     if res in my_cache:
#         return True
#     cache(a)

class CacheClass:

    def __init__(self):
        self.elems = []
        self.salt = 'any_salt'

    def is_empty(self):
        return self.elems == []

    def chek_cache(self, a):
        res = hashlib.sha3_256(a.encode() + self.salt.encode()).hexdigest()
        if res in self.elems:
            return True
        self.elems.append(res)

    def pop_out(self):
        return self.elems.pop()

    def cache_size(self):
        return len(self.elems)





myCache = CacheClass()


a = 'https://geekbrains.ru/lessons/94281/homework'
my_cache = []

print(myCache.chek_cache(a))
print(myCache.is_empty())