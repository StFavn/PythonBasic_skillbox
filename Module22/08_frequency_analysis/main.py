def completion_dict(user_str, dict_frequency):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for sym in user_str:
        if sym in alphabet:
            sym = sym.lower()
            if sym in dict_frequency:
                dict_frequency[sym] += 1
            else:
                dict_frequency[sym] = 1


def get_value(x):
    return x[1]


def organize_data(dict_frequency):
    entire_num = sum(dict_frequency.values())
    sorted_list = []
    temp_list = []
    same_value = 0
    for key, value in sorted(dict_frequency.items(), key=get_value, reverse=True):
        if value == same_value:
            temp_list.append(key + ' ' + str(round(value / entire_num, 3)))
        else:
            temp_list.sort()
            if temp_list:
                sorted_list.extend(temp_list)
            same_value = value
            temp_list = [key + ' ' + str(round(value / entire_num, 3))]
    temp_list.sort()
    sorted_list.extend(temp_list)
    return sorted_list


def get_frequency_range():

    file_r = open('text.txt', 'r')
    user_str = file_r.read()
    file_r.close()

    dict_frequency = {}
    completion_dict(user_str, dict_frequency)
    sorted_list = organize_data(dict_frequency)

    file_w = open('analysis.txt', 'w')
    file_w.write('\n'.join(sorted_list))
    file_w.close()


if __name__ == '__main__':
    get_frequency_range()
