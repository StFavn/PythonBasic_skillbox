# geographical_data = {
#     input(f'{i}-я страна: '): input('Города: ').split()
#     for i in
#     range(1, 1 + int(input('Количество стран: ')))
# }

geographical_data = [
    input(f'{i}-я страна: ').split()
    for i in
    range(1, 1 + int(input('Количество стран: ')))
]

# for i in range(1, 3 + 1):
#     search_city = input(f'\n{i}-й город: ')
#
#     for country, cities in geographical_data.items():
#         if search_city in cities:
#             print(f'Город {search_city} расположен в стране', country)
#             break
#     else:
#         print(f'По городу {search_city} данных нет.')

for i in range(1, 3 + 1):
    search_city = input(f'\n{i}-й город: ')

    for country in geographical_data:
        if search_city in country:
            print(f'Город {search_city} расположен в стране', country[0])
            break
    else:
        print(f'По городу {search_city} данных нет.')
