import os


def get_letter_dict(letter, user_dict):
    if letter in user_dict:
        user_dict[letter] += 1
    else:
        user_dict[letter] = 1


def get_value(x):
    return x[1]


def counting_everything():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    file = open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r')

    letter_dict = {}
    strings, words, letters, flag_en_letter = 0, 0, 0, False
    for string in file:
        strings += 1
        for word in string.split():
            for symbol in word:
                if symbol in alphabet:
                    letters += 1
                    get_letter_dict(symbol.lower(), letter_dict)
                    flag_en_letter = True
            if flag_en_letter:
                words += 1
                flag_en_letter = False
    file.close()

    # for let in letter_dict:
    #     print(let, ':', letter_dict[let])

    return letters, words, strings, min(letter_dict.items(), key=get_value)[0]


num_letters, num_words, num_strings, rare_letter = counting_everything()
print('Количество букв в файле:', num_letters)
print('Количество слов в файле:', num_words)
print('Количество строк в файле:', num_strings)
print('Наиболее редкая буква:', rare_letter)

