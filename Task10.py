# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

import random

n = int(input("Задайте кол-во монеток: "))

if n > 0:
    coins = []
    for i in range(n):
        coin = random.randint(0, 1)
        coins.append(coin)

    orel = 0
    reshka = 0                   # 2nd argument & the whole cycle can be replaced with:
    for coin in coins:           # orel = coins.count(0)
        if coin == 1:            # reshka = len(coins) - orel
            orel += 1
        else:
            reshka += 1
    
    if orel > reshka:
        print(f'Лучше перевернуть решку {reshka} -> {coins}')
    elif orel == reshka:
        print('Монеток вверх решкой и гербом равное кол-во.')
    else:
        print(f'Лучше перевернуть орел {orel} -> {coins}')
else:
    print("Введите корректное кол-во.")
