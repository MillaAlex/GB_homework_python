# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

n = int(input("Enter qty of elements of set-1: "))
m = int(input("Enter qty of elements of set-2: "))

collection1 = set()
collection2 = set()

for i in range(n):
    number = random.randint(1, 25)
    collection1.add(number)
print(collection1)

for i in range(m):
    number = random.randint(1, 25)
    collection2.add(number)
print(collection2)

collection_union = collection1.union(collection2)
print(sorted(collection_union))
