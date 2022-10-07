def get_data_records():
    records = []
    num = int(input('Сколько записей вносится в протокол? '))
    print('Записи (результат и имя):')
    for i in range(1, 1 + num):
        records.append(tuple(input(f'{i}-я запись: ').split()))
    return records


def get_competition_results(num_place):
    results = dict()
    for _ in range(num_place):
        max_name, max_points = ('', 0)
        for points, name in data_records:
            if (name not in results) and (int(points) > int(max_points)):
                max_name, max_points = name, points
        results[max_name] = max_points
    return results


def print_results(results):
    print('\nИтоги соревнований:')
    place = 0
    for name, points in results.items():
        place += 1
        print(f'{place}-е место. {name} ({points})')


data_records = get_data_records()
competition_results = get_competition_results(3)
print_results(competition_results)
