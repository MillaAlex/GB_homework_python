# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
n = int(input("Задайте длину массива: "))
x = int(input("Введите заданное число Х: "))

list_numbers = []

for i in range(n):
    number = random.randint(0, 10)
    list_numbers.append(number)
print(list_numbers)

count = 1
flag = False
while flag is False:      # while not flag:
    if x in list_numbers:
        print(f"Число {x} самое близкое к x = {x}")
        flag = True
    elif x - count in list_numbers and x + count in list_numbers:
        print(f"Число {x - count} & {x + count} самое близкое к x = {x}")
        flag = True
    elif x - count in list_numbers:
        print(f"Число {x - count} самое близкое к x = {x}")
        flag = True
    elif x + count in list_numbers:
        print(f"Число {x + count} самое близкое к x = {x}")
        flag = True
    count += 1



# via def
def nearest_value(list_numbers, x):
    found = list_numbers[0]        
    for number in list_numbers:      
        if abs(number - x) < abs(found - x):
            found = number 
    return found 
 
print(f'Ближайшее число к {x} в списке {list_numbers} является {nearest_value(list_numbers, x)}')