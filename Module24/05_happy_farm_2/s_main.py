import random


class Farmer:
    def __init__(self, name='', garden=None, potates=0):
        self.name = name
        self.garden = garden
        self.potates = potates
    
    def get_info(self):
        print('{} | кортошек: {} '.format(self.name, self.potates), end='| ')
        self.garden.get_status()
        print('', end='| ')
    
    def work(self):
        self.garden.grow_up()
    
    def harvest(self):
        for i, v in enumerate(self.garden.row):
            if v == 4:
                self.garden.row[i] = 0
                self.potates += 1
    
    
class Garden:
    states = {0: '--', 1: '=-', 2: '==', 3: '@=', 4: '@@'}
    
    def __init__(self, row=[0, 0, 0, 0]):
        self.row = row
    
    def get_status(self):
        for i in self.row:
            print(self.states[i], end=' ')
    
    def grow_up(self):
        row_ind = [i for i in range(len(self.row))]
        random.shuffle(row_ind)
        for i in row_ind:
            if self.row[i] < 4:
                self.row[i] += 1
                break
    
    
class Game:  
    def __init__(self, garden=None, farmer=None):
        self.garden = garden
        self.farmer = farmer
    
    def help(self):
        print('-------------------------------------------------------------------------')
        print('Вам нужно много работать. Не беспокойтесь, скоро вы выполните всю работу!')
        print('w - работать')
        print('h - собирать урожай')
        print('help - помощь')
        print('exit - если вы вдруг решите отойти от дел.')
        print('-------------------------------------------------------------------------')
    
    def game(self):
        self.help()
        
        while True:   
            self.farmer.get_info()
            input_info = input('ввод: ')
            if input_info == 'exit':
                print('СПАСИБО ЗА ИГРУ!!!')
                break
            if input_info == 'help':
                self.help()
            if input_info == 'w':
                self.farmer.work()
            if input_info == 'h':
                self.farmer.harvest()                   


def game_init():   
    name = input('введите имя: ')
    garden = Garden()
    farmer = Farmer(name, garden) 
    game = Game(garden, farmer)
    game.game()
          

game_init()
