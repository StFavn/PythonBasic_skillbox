def print_dictionary(dictionary, output_text):
    print(output_text)
    for sym in sorted(dictionary.keys()):
        print(sym, ':', dictionary[sym])


text = input("Введите текст: ")

frequency = {}
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1

print_dictionary(frequency, '\nОригинальный словарь частот:')

inverted_frequency = {}
for letter, freq in frequency.items():
    if freq in inverted_frequency:
        inverted_frequency[freq].append(letter)
    else:
        inverted_frequency[freq] = [letter]

print_dictionary(inverted_frequency, '\nИнвертированный словарь частот:')
