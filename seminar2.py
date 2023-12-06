# Контекст
# След матрицы - это сумма чисел на её главной диагонали. След определён только для квадратных матриц
# (количество столбцов = количеству строк).
# Задача
# Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxN.

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sum = 0
# for i in range(len(matrix)):
#     sum = sum + matrix[i][i]
# print(sum) 

# Условие
# На вход подается число в десятичной системе счисления
# ● Задача
# Написать скрипт в любой парадигме, который возвращает полученное число переведенное в двоичную
# систему счисления. Обоснуйте сделанный выбор парадигм.
# ● Решение .. ?

# num = 217

# def to_binary(number):
#     result = " "
#     ost = 0
#     while number // 2 != 0:
#         print(number)
#         result = result + " " + str(number % 2)
#         number = number // 2
#     result = result + " " + str(number % 2)
#     reverse_result = result[::-1]
#     return  reverse_result     

# print(to_binary(num))

def to_base(num_dec: int, base: int): 
    result = []
    while num_dec > 0:
        num = num_dec % base
        if num < 10:
            result.append(str(num))
        else:
            result.append(chr(num + 55)) #преоразование числа в символ
        num_dec //= base
    return ''.join(reversed(result)) if result else "0"  

a = 26
b = 16
f = to_base(a, b)
print(f)             