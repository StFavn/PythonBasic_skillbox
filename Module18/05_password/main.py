while True:
    password = input('\nПридумайте пароль: ')
    if len(password) < 8:
        print('Пароль ненадёжный. Надо минимум 8 символов. Попробуйте ещё раз.')
    elif len([symbol for symbol in password if symbol.isdigit()]) < 3:
        print('Пароль ненадёжный. Надо минимум 3 цифры. Попробуйте ещё раз.')
    elif len([symbol for symbol in password if symbol.isupper()]) < 1:
        print('Пароль ненадёжный. Надо минимум 1 большая буква. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
