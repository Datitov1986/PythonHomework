import random

#---------------------TASK 1------------------------------------------------------------------------
#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# digit = input('Введите число: ')
# sum = 0
# for i in digit:
#     if i != '.':
#         sum += int(i)
# print(sum)

#---------------------TASK 2------------------------------------------------------------------------
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите число '))
#
# mult = 1
# for i in range(N - 1):
#     i = i + 1
#     mult = i * mult
#     print(mult, end=", ")
# print(mult * N)

#---------------------TASK 3------------------------------------------------------------------------
# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# list = []
# summ = 0
# n = int(input('Введите число: '))
# for i in range(1, n + 1):
#     summ += (1 + 1/i)**i
#
# print(summ)

#---------------------TASK 4------------------------------------------------------------------------
# *4. НЕОБЯЗАТЕЛЬНАЯ ЗАДАЧА
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import *
# list = []
# n = int(input('Введите число: '))
# for _ in range(n):
#     list.append(randint(-n, n))
# print(list)
# with open ('file.txt', 'w', encoding='utf=8') as f:
#     for _ in range(randint(1, n)):
#         f.write(str(randint(0, n - 1)) + '\n')
# fact = 1
# with open ('file.txt', 'r', encoding='utf=8') as f:
#     f = f.read().splitlines()
#     for number in f:
#         fact *= list[int(number)]
# print(fact)

#---------------------TASK 5------------------------------------------------------------------------
# Реализуйте алгоритм перемешивания списка.

# import time
# now = time.time()
# print(now)
#
# list = [1, 4, 9, 10]
# # random.shuffle(list)
# # print(list)
# for i in range(random.randint(1, 10)):
#     i1 = random.randint(0, len(list) - 1)
#     i2 = random.randint(0, len(list) - 1)
#     list[i1], list[i2] = list[i2], list[i1]
# print(list)


# import time
# random_number = str(time.time()).split('.')[1]
# list = [1, 4, 9, 10]
# for i in range(int(str(time.time()).split('.')[1]) % (10 - 5 + 1) + 5):
#     i1 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
#     time.sleep(0.00001)
#     i2 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
#     list[i1], list[i2] = list[i2], list[i1]
# print(list)

# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

