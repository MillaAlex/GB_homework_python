# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке.
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

#Вар.1 - без функции
vinnis_poem = input("Введите стихотворение Винни-Пуха: ")
poem = vinnis_poem.split()

vowels = 'аеиоуыэюя'
count = 0
for i in poem:
    for j in i:
        if j in vowels:
            count +=1
#print(count)
if count % 2 == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')

#////////////////////////////////////////////////////////

#Вар.2 - с функцией
vinnis_poem = input("Введите стихотворение Винни-Пуха: ")
poem = vinnis_poem.split()

def rythm(poem):
    vowels = 'аеиоуыэюя'
    check_vowel = lambda x: sum(1 for i in x if i in vowels)
    temp = check_vowel(poem[0])
    if all([check_vowel(i) == temp and temp % 2 == 0 for i in poem]):
        return('Парам пам-пам')
    return('Пам парам')
print(rythm(poem))
