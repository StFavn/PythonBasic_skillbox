import random


class Cards:
    points = {'Туз': 11, 'Двойка': 2, 'Тройка': 3, 'Четверка': 4, 'Пятерка': 5, 'Шестерка': 6,
              'Семерка': 7, 'Восьмерка': 8, 'Девятка': 9, 'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10}

    deck_cards = [card for card in points for _ in range(4)]
    random.shuffle(deck_cards)

    def take_a_card(self):
        try:
            self.cards.append(self.deck_cards[0])
        except IndexError:
            print('Колода закончилась.')
        self.deck_cards.remove(self.deck_cards[0])

    def __init__(self, name='', cards=None):
        self.name = name
        self.cards = cards or []
        for _ in range(2):
            self.take_a_card()

    def count_points(self):
        num_points = 0
        for card in self.cards:
            if card == 'Туз' and num_points > 21:
                num_points += 1
            else:
                num_points += self.points[card]
        return num_points

    def view_cards(self):
        print(', '.join(self.cards))


def game():
    computer = Cards('computer')
    user = Cards('user')
    print('На руке: ', end='')
    user.view_cards()

    while input('Еще карту? (да/нет): ').lower().startswith('да'):
        user.take_a_card()
        print('На руке: ', end='')
        user.view_cards()

    user_points = user.count_points()
    computer_points = computer.count_points()
    if user_points > 21 or user_points < computer_points:
        print(f'Вы проиграли, набрав {user_points} очков, компьютер же набрал {computer_points}.')
    elif user_points > computer_points:
        print(f'Вы выиграли, набрав {user_points} очков, компьютер же набрал {computer_points}.')
    else:
        print(f'Ничья, вы и компьютер набрали по {user_points}.')
    print('Карты компьютера: ', end='')
    computer.view_cards()


game()
