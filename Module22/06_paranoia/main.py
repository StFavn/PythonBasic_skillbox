def change(user_str, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_str = ''
    for symbol in user_str:
        if symbol in alphabet:
            old_index = alphabet.index(symbol)
            new_str += alphabet[(old_index + n) % 26 + (old_index // 26) * 26]
        else:
            new_str += symbol
    return new_str


def caesar_cipher():
    file_r = open('text.txt', 'r')
    file_w = open('cipher_text.txt', 'w')
    for i, i_str in enumerate(file_r):
        new_i_str = change(i_str, i + 1)
        file_w.write(new_i_str)
    file_r.close()
    file_w.close()


if __name__ == '__main__':
    caesar_cipher()
