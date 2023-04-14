# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите n: "))
m = int(input("Введите m: "))
k = int(input("Введите k: "))

size = n * m

if size > k:
    if (k % n == 0 or k % m == 0):
        print(f"Можно отломить {k} долек одним разломом по прямой между дольками.")
    else:
        print(f"Нельзя отломить {k} долек одним разломом по прямой между дольками.")
else:
    print("Нельзя.")