def delete_end_n(bad_point):
    point = ''
    for sym in bad_point:
        if sym != '\n':
            point += sym
    return int(point)


def get_points(x):
    return int(x[2])


def get_data():
    file_r = open('first_tour.txt', 'r')

    list_data, pass_point = [], 0
    for i, i_str in enumerate(file_r):
        if i == 0:
            pass_point = delete_end_n(i_str)
        else:
            list_data.append(i_str.split())
    file_r.close()
    return pass_point, list_data


def change_data(pass_point, list_data):
    new_list = []
    for member in list_data:
        points = delete_end_n(member[2])
        if points > pass_point:
            new_list.append([member[1][0] + '.', member[0], str(points)])
    new_list.sort(key=get_points, reverse=True)
    return new_list


def transition():

    pass_point, list_data = get_data()
    new_data_list = change_data(pass_point, list_data)

    file_w = open('second_tour.txt', 'w')
    file_w.write(str(len(new_data_list)))
    for i, i_elem in enumerate(new_data_list):
        file_w.write('\n{0}) '.format(i + 1) + ' '.join(i_elem))
    file_w.close()
