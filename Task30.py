# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def fill_array():
    math_progresson_array = []
    for i in range(elements_qty):
        num = element_1 + i * difference
        math_progresson_array.append(num)
    return math_progresson_array

element_1 = int(input("Enter 1st element: "))
difference = int(input("Enter difference: "))
elements_qty = int(input("Enter quantity of element: "))

print(result_array:= fill_array())
