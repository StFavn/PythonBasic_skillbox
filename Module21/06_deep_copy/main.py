def create_site(product):

    site = {
        'html': {
            'head': {
                'title': f'Куплю/продам {product} недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {product}',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }

    return site


def deep_copying(num, site_list={}):

    if num < 1:
        return
    deep_copying(num - 1)

    product = input('Введите название продукта для нового сайта: ')
    site_list[f'\nСайт для {product}:'] = create_site(product)

    for title, site in site_list.items():
        print(title, '\n', site, '\n')


deep_copying(int(input('Сколько сайтов: ')))

