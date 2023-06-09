# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# optin 1 - with int:

number = int(input("Введите 6-значное число: "))
sum1 = 0
sum2 = 0

if 99999 < number < 1000000:

    part1 = number // 1000
    while part1 > 0:
        temp1 = part1 % 10
        sum1 += temp1
        part1 //= 10

    part2 = number % 1000
    while part2 > 0:
        temp2 = part2 % 10
        sum2 += temp2
        part2 //= 10

    if sum1 == sum2:
        print(f"Билет с номером {number} счастливый.")
    else:
        print(f"Билет с номером {number} не счастливый.")
else:
    print("Введено не 6-значное число.")


# optin 2 - with string:

number = input("Введите 6-значное число: ")
res1 = 0
res2 = 0
if len(number) == 6:
    for i in range(len(number) // 2):
        res1 += int(number[i])
        res2 += int(number[-i - 1])
    print(res1, res2)
    if res1 == res2:
        print("yes")
    else:
        print("no")
else:
    print("Введено не 6-значное число.")
