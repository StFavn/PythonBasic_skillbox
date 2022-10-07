contacts = {}

while True:

    print('\nВведите номер действия:\n 1. Добавить контакт\n 2. Найти человека')
    command = input('')

    if command == '1':
        name_n_surname = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
        if name_n_surname not in contacts:
            contacts[name_n_surname] = int(input("Введите номер телефона: "))
        else:
            print('Такой человек уже есть в контактах.')
        print('Текущий словарь контактов:', contacts)

    elif command == '2':
        surname_search = input('Введите фамилию для поиска: ').title()
        if surname_search.endswith('а'):
            surname_search = ''.join(list(surname_search)[: -1])
        for full_name, num in contacts.items():
            name, surname = full_name
            if surname_search in surname.title():
                print(name, surname, num)

    else:
        print('Неправильная команда.')
