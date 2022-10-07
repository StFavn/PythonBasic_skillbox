import random


class Gardener:
    def __init__(self, name='', garden=None):
        self.name = name
        self.garden = garden
        self.num_potato = 0
        self.money = 0

    def get_info(self):
        print('{}: (Деньги {}, Уражай {}, '.format(self.name, self.money, self.num_potato), end='')
        self.garden.print_all_states()
        print('], уровень состояния: {}))'.format(self.garden.condition))

    def work_in_garden(self):
        self.garden.condition += 2
        self.garden.time_tick()

    def harvest(self):
        for index, potato in enumerate(self.garden.potatoes):
            if potato.is_ripe():
                self.garden.potatoes[index] = Potato(index)
                self.num_potato += 1
        self.garden.natural()

    def sell_potato(self):
        self.money += self.num_potato * 20
        self.num_potato = 0
        self.garden.time_tick()

    def pay_expansion(self):
        if self.money >= 100:
            self.money -= 100
            self.garden.potatoes.append(Potato(len(self.garden.potatoes)))
            self.garden.natural()
        else:
            print('Недостаточно денег для покупки грядки.')


class Potato:
    states = {0: '───', 1: '─┬─', 2: '─┼─', 3: '❿┼❿'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self, condition):
        if self.state < 3 and random.randint(0, condition) != 0:
            self.state += 1

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(Potato.states[self.state], end=' ')


class PotatoGarden:
    def __init__(self, count=5, condition=0):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]
        self.condition = condition

    def natural(self):
        if self.condition > 0:
            self.condition -= 1

    def time_tick(self):
        for potato in self.potatoes:
            potato.grow(self.condition)
        self.natural()

    def are_all_ripe(self):
        if all([potato.is_ripe() for potato in self.potatoes]):
            return True
        else:
            return False

    def print_all_states(self):
        print('Ваш огород: [', end='')
        for potato in self.potatoes:
            potato.print_state()


def game():
    print('МОЯ ФЕРМА'.center(100, '-'))

    player = Gardener(input('Имя вашего фермера: '), PotatoGarden())
    help_full = '-' * 100 + '\nРазвивайте ваш огород с помощью команд:\n' \
                            '"w" - (work)    Работать в огороде\n' \
                            '"h" - (harvest) Собирать уражай\n' \
                            '"s" - (sale)    Продавать картошку по цене 20\n' \
                            '"p" - (pay)     Покупать грядку за 100\n' \
                            '"r" - (rest)    Просто отдохнуть\n ' \
                            'ЗАДАНИЕ: расширьте ваш огород до 10-ти грядок.\n' + '-' * 100
    print(help_full)

    while len(player.garden.potatoes) < 10:
        player.get_info()
        act = input('Ваше действие: ')
        if act == 'w':
            player.work_in_garden()
        elif act == 'h':
            player.harvest()
        elif act == 's':
            player.sell_potato()
        elif act == 'p':
            player.pay_expansion()
        elif act == 'r':
            print('-' * 100)
            print('Вы, конечно, отдохнули, но состояние огорода от этого лучше не стало.')
            player.garden.time_tick()
        elif act == 'help':
            print(help_full)
        else:
            print('Нет такой команды. Посмотрите список команд "help".')
        print('-' * 100)
    print('ВЫ ВЫИГРАЛИ'.center(100, '-'))
    print('Ваше итоговое состояние:')
    player.get_info()


game()
