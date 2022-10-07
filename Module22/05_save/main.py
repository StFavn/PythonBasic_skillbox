import os


def save_text(text):
    path = os.path.join(os.path.splitdrive(os.getcwd())[0], '\\')
    # path_str = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n')
    path_str = 'Users Efrem Desktop Python_Basic Module22'
    for direct in path_str.split():
        if direct in os.listdir(path):
            path = os.path.join(path, direct)
        else:
            print('Нет директория', direct, 'по адресу:', path)
            return

    file_name = input('\nВведите имя файла: ')
    find = file_name in os.listdir(path)
    if not find or (find and input('Вы действительно хотите перезаписать файл (да/нет)? - ') == 'да'):
        file = open(os.path.join(path, file_name + '.txt'), 'w')
        file.write(text)
        file.close()
        if find:
            print('Файл успешно перезаписан!')
        else:
            print('Файл успешно сохранен!')
    else:
        print('Файл не был перезаписан!')


save_text(input('Введите строку: '))
