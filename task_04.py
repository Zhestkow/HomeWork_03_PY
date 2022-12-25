# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# print(bin(int(input('Введите число ')))[2:])


import os
import random as r
def clear(): return os.system('cls')

clear()

n = int(input('Введите число -> '))
def to_bin(n,res=''):
    if n==0:
        return res
    res=str(n%2)+res
    return to_bin(n//2,res)

print(to_bin(n))