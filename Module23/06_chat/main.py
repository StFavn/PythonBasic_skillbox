import os


def search_contact(name):
    if os.path.exists('users.txt'):
        with open('users.txt', 'r', encoding='utf-8') as users:
            for user in users:
                user_name, user_password = tuple(user.rstrip().split())
                if name == user_name:
                    return user_password
    return ''


def create_contact(name):
    if input('Вы новый пользователь? ').lower() == 'да':
        password = input('Придумайте пароль: ')
        while ' ' in password:
            password = input('В пароле не должно быть пробелов: ')
        with open('users.txt', 'ab') as users:
            users.write((name + ' ' + password + '\n').encode(encoding='utf-8'))
        return True
    return False


def get_contact():
    while True:
        name = input('\nНик: ')
        user_password = search_contact(name)
        if user_password:
            password = input('Пароль: ')
            if password == user_password:
                return name
            else:
                print('Неверный пароль!')
        else:
            print('Такого имени нет. ', end='')
            if create_contact(name):
                return name


def show_text():
    print()
    if os.path.exists('chat.txt'):
        with open('chat.txt', 'r', encoding='utf-8') as chat:
            for replica in chat:
                print(replica, end='')
    else:
        print('Пока здесь ничего нет. Напишите первым!')
    print()


def add_massage(name, massage):
    with open('chat.txt', 'ab') as chat:
        chat.write(f'{name}:\t{massage}\n'.encode(encoding='utf-8'))


try:
    nick_name = get_contact()
    print('Введите "чат", для просмотра чата.')
    while True:
        act = input('Сообщение (или "чат"): ')
        if act == 'чат':
            show_text()
        else:
            add_massage(nick_name, act)
except UnicodeError:
    print('Ну вот, ваш символ все сломал, перезайдите в чат.')  # Хотя на самом деле, декодится даже "♞"
except PermissionError:
    print('К сожалению, ваш компьютер находится в бане. Обратитесь в тех. поддержку.')
except Exception as exc:
    print('Чат, почему-то не работает. Обратитесь в тех. поддержку, скажите:', exc)
