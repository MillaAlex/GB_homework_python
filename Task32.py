# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def find_indexes():
    my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    result_list = []
    for i in range(len(my_list)):
        if my_list[i] >= min_value and my_list[i] <= max_value:
            result_list.append(i)
    return result_list

min_value = int(input("Enter min: "))
max_value = int(input("Enter max: "))

print(find_indexes())
