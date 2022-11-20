#---------------------------TASK 1-------------------------------------
# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

# a,b = [1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]
# list = []
# for i in range(len(a)):
#     for e in range(len(b)):
#         if a[i] == b[e]:
#             list.append(b[e])
# print(list)

#---------------------------TASK 2-------------------------------------
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

# k = int(input('Введите число: '))
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# for i in range(k):
#     print(fibonacci(i))

# print(fibonacci)

# n = int(input('Введите число: '))

# def fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n + 1):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums
#
# fibo_nums = fibonacci(n)
# print(fibonacci(n))

# # Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

num = input('введите число от 0 до 10 по английски: ')
number = num.capitalize()

def translate(number):

    eng_to_rus_translate = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре', 'Five': 'пять',
                            'Six': 'шесть', 'Seven': 'семь', 'Eight': 'восемь', 'Nine': 'девять',
                            'Ten': 'десять', 'Zero': 'ноль'}
    if number not in eng_to_rus_translate:
        print('None')
    else:
        print(f'{number} по русски: {eng_to_rus_translate[number].capitalize()}')

translate(number)



# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

# def thesaurus_adv(*args):
#     some_list = list(args)
#     some_dict = {}
#     for i in range(len(some_list)):
#         if some_list[i][0] in some_dict.keys():
#             some_dict[some_list[i][0]].append(some_list[i])
#         else:
#             some_dict[some_list[i][0]] = [some_list[i]]
#     print(some_dict)
#
#
#
#
# thesaurus_adv("Иван", "Мария", "Петр", "Илья", "Петро", "Федор")
