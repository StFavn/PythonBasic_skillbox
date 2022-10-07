def reverse_text(text):
    return '\n'.join(text.split('\n')[::-1])


def get_text():
    file = open('zen.txt', 'r')
    text = file.read()
    file.close()
    return text


if __name__ == '__main__':
    truth_list = get_text()
    print(reverse_text(truth_list))

