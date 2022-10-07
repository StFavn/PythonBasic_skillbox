entire_vowel = ['a', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']

text = list(input('Введите текст: '))  # Нужно отнести кольцо в Мордор!
list_vowel_letters = [symbol for symbol in text if symbol in entire_vowel]

print('\nСписок гласных букв:', list_vowel_letters)
print('Длина списка:', len(list_vowel_letters))

# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
#
# Длина списка: 9