#---------------------------TASK 1-------------------------------------
# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

a,b = [1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]
list = []
for i in range(len(a)):
    for e in range(len(b)):
        if a[i] == b[e]:
            list.append(b[e])
print(list)

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

n = int(input('Введите число: '))

def fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n + 1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = fibonacci(n)
print(fibonacci(n))
    
