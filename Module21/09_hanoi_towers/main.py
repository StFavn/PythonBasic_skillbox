def create_picture(n, x, picture):
    for i in range(1, 4):
        if i == x:
            picture.append(list(range(n, 0, -1)))
        else:
            picture.append([])
    picture.append(n)


def show(picture):
    show_list = ''
    for i in range(3):
        show_list += ''.join([str(element) for element in picture[i]]) + \
                     '-' * (picture[-1:][0] - len(picture[i])) + ' | '
    return show_list


def move(n, x, y, picture=[]):
    if not picture:
        create_picture(n, x, picture)
        print('| Ханойские башни |    | ' + show(picture))
    if n == 1:
        picture[y - 1].append(picture[x - 1].pop())
        print(f'| 1-й: "{x}" -> "{y}" |    | ' + show(picture))
    else:
        move(n - 1, x, 6 - x - y, picture)
        picture[y - 1].append(picture[x - 1].pop())
        print(f'| {n}-й: "{x}" -> "{y}" |    | ' + show(picture))
        move(n - 1, 6 - x - y, y, picture)


move(9, 1, 3)
