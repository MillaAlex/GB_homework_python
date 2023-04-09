# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

totalNum = int(input("Всего сделано журавликов: "))
if totalNum % 6 != 0:
    print("Некорректное количество.")
else:
    temp = totalNum // 3
    print(f"Петя сделал {temp // 2} журавликов")
    print(f"Катя сделала {totalNum - temp} журавликов")
    print(f"Сережа сделал {temp // 2} журавликов")
