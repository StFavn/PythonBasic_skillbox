def name_start_sign(name):
    signs = '@№$%^&\*()'
    for sign in signs:
        if file_name.startswith(sign):
            return True
    return False


file_name = input('Название файла: ')
if name_start_sign(file_name):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_name.endswith('.txt') and not file_name.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')
