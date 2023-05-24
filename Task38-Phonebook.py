# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def add_contact(f):
    input_name = input('Введите имя: ')
    input_lastname = input('Введите фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_lastname}; {input_name}; {input_phone}' 
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} успешно добавлена.')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list


def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)


def search_contact(f):
    lastname = input('Введите фамилию или имя для поиска: ')
    adr_book = read_all(f)
    for line in adr_book:
        if lastname in line:
            print(line)


def change_data(f):
    adr_book = read_all(f)
    print(f'Всего контактов в справочнике: {len(adr_book)}')
    for i in range(len(adr_book)):
        print(i, adr_book[i])
    idx = int(input('Введите индекс контакта для замены: '))
    for idx in adr_book:
        while True:
            user_changes = input('Выберите: \n1 - изменить фамилию,\n2 - изменить телефон,\n'
                                'Имя изменить нельзя.\n3 - удалить запись, \nq - для перехода в главное меню. \n')
            if user_changes == '1':
                name, phone = adr_book[i].split('; ')[1:]
                lastname = input('Введите новую фамилию: ')
                new_record = f'{lastname}; {name}; {phone}'
                adr_book[i] = new_record
                with open(f, 'w', encoding='utf-8') as fd:
                    fd.writelines(adr_book)
                print('Запись успешно изменена.')
            elif user_changes == '2':
                lastname, name = adr_book[i].split('; ')[:2]
                phone = input('Введите новый телефон: ')
                new_record = f'{lastname}; {name}; {phone}'
                adr_book[i] = new_record
                with open(f, 'w', encoding='utf-8') as fd:
                    fd.writelines(adr_book)
                print('Запись успешно изменена.')
            elif user_changes == '3':
                new_record = ''
                adr_book[i] = new_record
                with open(f, 'w', encoding='utf-8') as fd:
                    fd.writelines(adr_book)
                print('Запись успешно удалена.')
            elif user_changes == 'q':
                print('Выход из подменю выполнен.')
            main()
            break


def main():
    file = 'phone_book.txt'
    while True:
        user_choice = input('Выберите действие: \n'
                            '1 - добавить запись,\n2 - прочитать всю тел.книгу,\n'
                            '3 - найти запись, \n4 - изменить или удалить запись, \nz - нажмите для выхода. \n')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            change_data(file)   
        elif user_choice == 'z':
            print('Всего хорошего.')
            break

if __name__ == '__main__':
    main()