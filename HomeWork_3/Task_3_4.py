#4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт разницу между максимальным и 
#минимальным значением дробной части элементов.

from random import uniform


n = int(input('Введите размер списка '))
list1 = []
for i in range(n):
    f = uniform(0, 9)
    list1.append(round(f, 2))

min = list1[0]
max = 0
for i in range(len(list1)):

    if max < list1[i]:
        max = list1[i]
    if min > list1[i]:
        min = list1[i]
dif = (max - int(max)) - (min - int(min))

print(list1)
print(max, min)
print(round(dif, 2))
