# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import os
import random as r
def clear(): return os.system('cls')


clear()


n = int(input('Введите число -> '))
num = [r.randint(-n, n) for i in range(n)]
print(num)
s = []
sum = 0
for i in range(n//2+n % 2):
    sum = num[i]*num[-i-1]
    print(sum, end=(' '))
