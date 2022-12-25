# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12






import os, random as r
clear = lambda: os.system('cls')
clear()


n = int(input('Введите число -> '))
num = [r.randint(-n,n) for i in range(n)]
print(num)
sum=0
for i in range(1, n, 2):
    sum = sum + (num[i])
print(sum)