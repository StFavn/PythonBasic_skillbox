import zipfile
import os


def unpacking(zip_file):
    old_files = ['statistics.txt']
    path_that_dir = os.path.join(os.path.abspath(zip_file), '..')
    for file_name in os.listdir(path_that_dir):
        old_files.append(file_name)

    if zipfile.is_zipfile(zip_file):
        war_peace_zip = zipfile.ZipFile(zip_file, 'r')
        war_peace_zip.extractall()
        war_peace_zip.close()

    for file_name in os.listdir(path_that_dir):
        if file_name not in old_files:
            return file_name
    return None


def completion_dict(user_file):
    dict_frequency = {}
    alphabet = \
        'abcdefghijklmnopqrstuvwxyz' \
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' \
        'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    sym = user_file.read(1)
    while sym:
        if sym in alphabet:
            if sym in dict_frequency:
                dict_frequency[sym] += 1
            else:
                dict_frequency[sym] = 1
        sym = user_file.read(1)

    return dict_frequency


def get_value(x):
    return x[1]


def form_str(key, value, entire_num):
    return key + ': num = ' + str(value) + ', freq = ' + str(round(value / entire_num, 6))


def organize_data(dict_frequency):
    entire_num = sum(dict_frequency.values())
    sorted_list = []
    temp_list = []
    same_value = 0
    for key, value in sorted(dict_frequency.items(), key=get_value, reverse=True):
        if value == same_value:
            temp_list.append(form_str(key, value, entire_num))
        else:
            temp_list.sort()
            if temp_list:
                sorted_list.extend(temp_list)
            same_value = value
            temp_list = [form_str(key, value, entire_num)]
    temp_list.sort()
    sorted_list.extend(temp_list)
    return sorted_list


def counting_letters(user_path):

    war_peace_file = open(user_path, 'r', encoding='utf-8')
    dict_frequency = completion_dict(war_peace_file)
    war_peace_file.close()

    sorted_list = organize_data(dict_frequency)

    result_file = open('statistics.txt', 'wb')
    result_file.write('\n'.join(sorted_list).encode('utf-8'))
    result_file.close()


war_and_peace = unpacking('voyna-i-mir.zip')
if war_and_peace:
    counting_letters(war_and_peace)
else:
    print('Ничего нового в zip-файле не было')
