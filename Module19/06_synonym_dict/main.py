
synonyms_dictionary = dict()
for i in range(1, 1 + int(input('Введите количество пар слов: '))):

    while True:
        words_couple = input(f'{i}-я пара: ').split()
        if len(words_couple) == 3:
            break
        print('Пара - это два слова через дефис или тире. Например: "Весело — Радостно"')
    synonyms_dictionary[words_couple[0]] = words_couple[2]

while True:
    a_word = input('\nВведите слово: ')
    for fst_word, sec_word in synonyms_dictionary.items():
        if a_word.lower() == fst_word.lower():
            print('Синоним:', sec_word)
            break
        if a_word.lower() == sec_word.lower():
            print('Синоним:', fst_word)
            break
    else:
        print('Такого слова в словаре нет.')
        continue
    break
