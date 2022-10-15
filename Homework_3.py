
#---------------------------------------TASK 1----------------------------------------------------
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import *
# list = []
# n = int(input('Введите число: '))
# summ = 0
# for _ in range(n):
#     list.append(randint(1, n))
# print(list)
# for i in range(0, n):
#     if i % 2 == 0:
#         i += 1
#     else:
#         summ = summ + list[i]
#         i += 1
# print(summ)

#---------------------------------------TASK 2----------------------------------------------------
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import *
# list = []
# list2 = []
# n = int(input('Введите число: '))
# for _ in range(n):
#     list.append(randint(1, 10))

# for i in range(len(list)):
#     while i < len(list)/2 and n > len(list)/2:
#         n = n - 1
#         list2.append(list[i] * list[n])
#         i += 1
# print(list)  
# print(list2)

#---------------------------------------TASK 3----------------------------------------------------
#Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import *

# n = int(input('Введите размер списка '))
# list = []
# new_list = []
# for i in range(n):
#     f = uniform(0, 9)
#     list.append(round(f, 2))
# for i in range(len(list)):
#     new_list.append(int((list[i] * 100)% 100))

# min = new_list[0]
# max = 0
    
# for i in range(len(new_list)):   
#     if max < new_list[i]:
#         max = new_list[i]
#     if min > new_list[i]:
#         min = new_list[i]
# dif = float((max - min)/100)

# print(list)
# print(float(max/100), float(min/100))
# print(round(dif,2))

#---------------------------------------TASK 4----------------------------------------------------    

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#--VAR 1---------------------------------------------

# number_10 = int(input('Введите число: '))
# dif_number = number_10
# number_2 = []
# while dif_number >= 1:
#     number_2.append(int(dif_number%2))
#     dif_number = dif_number / 2
# #number_2.reverse()                  
# number_2_correct = number_2[::-1]
# print(number_2_correct)


#--VAR 2--------------------------------------

# number_10 = int(input('Введите число: '))
# print(bin(number_10))

#--VAR 3--------------------------------------

# number_10 = int(input('Введите число: '))
# number_2 = ''
# while number_10 > 0:
#     number_2 = str(number_10 % 2) + number_2
#     number_10 = number_10 // 2
# print(number_2)
