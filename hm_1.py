#Задача №1
#Дан список целых чисел numbers. 
#Необходимо написать в императивном стиле процедуру для сортировки числа в списке в порядке убывания. 
#Можно использовать любой алгоритм сортировки.

numbers_list = [2, 14, 1, 4, 6, 5, 18]

def sort_list_imperative(numbers): 
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers            

print(sort_list_imperative(numbers_list))

#Задача №2
#Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

print(sort_list_declarative(numbers_list))
