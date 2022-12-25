# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import os
import random as r
def clear(): return os.system('cls')


clear()


n = int(input('Введите число -> '))
list = [round(r.uniform(1, n),2) for i in range(n)]
print(list)
max=round(list[0]%1,2)
min=round(list[0]%1,2)
for i in range(n):
    # print(round(list[i]%1,2), end=(' '))
    if round(list[i]%1,2)>max:
        max = round(list[i]%1,2)
    elif round(list[i]%1,2)<min:
        min = round(list[i]%1,2)
print(max,min)
print(round((max-min),2))
