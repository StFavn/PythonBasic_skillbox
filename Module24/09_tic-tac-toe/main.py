class Cell:
    def __init__(self, index, symbol='   '):
        self.index = index
        self.symbol = symbol

    def occupied(self):
        if self.symbol == '   ':
            return False
        return True


class Board:
    board_help = [[Cell(i, str(i + 1)) for i in range(j*3, j*3 + 3)] for j in range(3)]
    board = [[Cell(i) for i in range(j*3, j*3 + 3)] for j in range(3)]

    def show(self):
        board_str = [[self.board[j][i].symbol for i in range(3)] for j in range(3)]
        print('\n---|---|---\n'.join(['|'.join(board_str[i]) for i in range(3)]))

    def is_win(self, symbol):
        for j in range(3):
            if all([self.board[i][j].symbol == symbol for i in range(3)]):
                return True
        for i in range(3):
            if all([self.board[i][j].symbol == symbol for j in range(3)]):
                return True
        if all([self.board[i][i].symbol == symbol for i in range(3)]):
            return True
        if all([self.board[i][2 - i].symbol == symbol for i in range(3)]):
            return True
        return False


class Player:
    def __init__(self, symbol=' ', game=Board()):
        self.symbol = symbol
        self.game = game

    def move(self, index):
        if not self.game.board[(index-1) // 3][(index-1) % 3].occupied():
            self.game.board[(index-1) // 3][(index-1) % 3].symbol = self.symbol
            return True
        return False


def show_help():
    print('\nВведите цифру, на место которой хотите нарисовать свой символ:')
    print(' 1 | 2 | 3 ')
    print('---|---|---')
    print(' 4 | 5 | 6 ')
    print('---|---|---')
    print(' 7 | 8 | 9 ')


def play(player):
    try:
        if not player.move(int(input(f'Ход {player.symbol}: '))):
            print('Это место занято')
            play(player)
        else:
            player_one.game.show()
    except IndexError:
        print('Нет такой ячейки')
        play(player)


player_one = Player(' X ')
player_two = Player(' 0 ')
show_help()
while True:
    play(player_one)
    if player_one.game.is_win(player_one.symbol):
        print('Победитель:', player_one.symbol)
        break
    play(player_two)
    if player_two.game.is_win(player_two.symbol):
        print('Победитель:', player_two.symbol)
        break

