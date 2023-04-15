# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3 -> 1

import random
n = int(input("Задайте длину массива: "))
x = int(input("Введите искомое число Х: "))

count = 0
list_numbers = []

for i in range(n):
    number = random.randint(0, 10)
    list_numbers.append(number)
print(list_numbers)
for i in range(0, len(list_numbers)):
    if list_numbers[i] == x:
        count += 1
print(f"Число {x} -> {count} раз(а)")
