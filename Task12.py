# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

#1 cycle
for i in range(1, 1000):
    if i * (s - i) == p:
        print(f"Загаданные числа: {i}, {s - i}")
        break
else:
    print("Некорректное число")

# #2 cycles:
# for i in range(1, 1000):
#     for j in range(1, 1000):
#         if i + j == s and i * j == p:
#             print(f"Загаданные числа: {i}, {j}")
#             break
# else:
#     print("Некорректное число")
