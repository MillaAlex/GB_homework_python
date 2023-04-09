# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите число: "))
summa = 0

while number > 0:
    temp = number % 10
    summa += temp
    number //= 10
print(summa)
