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
for i in range(0, len(list_numbers)):
    if list_numbers[i] == x:
        print(f"Число {list_numbers[i]} самое близкое к x = {x}")
        break
    elif (list_numbers[i] == x + 1) or (list_numbers[i] == x - 1):
        print(f"Число {list_numbers[i]} самое близкое к x = {x}")
        break
