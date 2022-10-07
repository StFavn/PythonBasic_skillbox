def chack_year(year, n):
    if year == '':
        return False
    year_short = ''
    for sample in year:
        num = 0
        for symbol in year:
            if symbol == sample:
                num += 1
            else:
                year_short += symbol
            if num == n:
                return True
        if chack_year(year_short, n):
            return True
        else:
            return False


first_year = int(input('Начальный год: '))
last_year = int(input('Конечный год: '))
while last_year < first_year:
    print('Конечный год должен быть меньше начального.')
    first_year = int(input('Начальный год: '))
    last_year = int(input('Конечный год: '))

coincidence = int(input('Совпадающих цифр: '))
while coincidence <= 0:
    print('Количество совпадающих цифр должно быть положительным значением.')
    coincidence = int(input('Совпадающих цифр: '))

for year in range(first_year, last_year + 1):
    if chack_year(str(year), coincidence):
        print(year)