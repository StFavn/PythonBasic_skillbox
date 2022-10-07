def print_nums(num):
    if num <= 0:
        return
    print_nums(num - 1)
    print(num)
    return


print_nums(int(input('Введите num: ')))
