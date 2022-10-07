def num_sum():
    file_r = open('numbers.txt', 'r')
    file_w = open('answer.txt', 'w')

    summa = sum([int(two) for two in file_r.read().split()])
    file_w.write(str(summa))

    file_r.close()
    file_w.close()


if __name__ == '__main__':
    num_sum()
