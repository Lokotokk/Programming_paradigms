# Условие
# На вход подается число n.
# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# Пример вывода:

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9


def multiplication_table(num):
    list_1 = []
    for i in range(1, num + 1):
        for j in range(1, 10):
            list_1.append(f'{i} х {j} = {i * j}')
    return print_table(list_1)

def print_table(some_list):
    for i in some_list:
        print(i)

n = 5
multiplication_table(n)   