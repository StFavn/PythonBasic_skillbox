def search_element(data, tag, deep_limit=0):
    if tag in data:
        return data[tag]
    if deep_limit == 1:
        return None
    for key, value in data.items():
        if isinstance(value, dict):
            result = search_element(value, tag, deep_limit - 1)
            if result:
                return result
    return None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

search_key = input('Введите искомый ключ: ')

if input('Хотите ввести максимальную глубину? Y/any_key: ').lower() == 'y':
    search_value = search_element(site, search_key, int(input('Введите максимальную глубину: ')))
else:
    search_value = search_element(site, search_key)

print('Значение ключа:', search_value)
