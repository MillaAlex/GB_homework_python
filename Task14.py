# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

#option 1:
n = int(input("Введите число N: "))
k = 1
i = 1
print(n, end=' ' "-> ")
while (i * k) <= n:
    print(i * k, end=' ')
    k *= 2
    
#option 2:
n = int(input("Введите число N: "))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
