# def coding_text_2(alphabet_list, text_str, shift):
#     cod_list = [alphabet_list[(alphabet_list.index(letter) + k) % 33]
#                 if letter in alphabet else letter for letter in text_str]
#     cod = ''
#     for sym in cod_list:
#         cod += sym
#     return cod


def coding_text_1(alphabet_list, text_str, shift):
    cod = ''
    for letter in text_str:
        if letter in alphabet_list:
            cod += alphabet_list[(alphabet_list.index(letter) + shift) % 33]
        else:
            cod += letter
    return cod


alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
    'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]
text = input('Введите сообщение: ')
k = int(input('Введите сдвиг: '))
print('Зашифрованное сообщение:', coding_text_1(alphabet, text, k))
# print('Зашифрованное сообщение:', coding_text_2(alphabet, text, k))