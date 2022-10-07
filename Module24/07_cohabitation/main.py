import random


class Human:
    def __init__(self, name='', home=None, satiety=50):
        self.name = name
        self.satiety = satiety
        self.home = home

    def game(self):
        self.satiety -= 1
        return 'играет'

    def eat(self):
        self.satiety += 1
        self.home.meal -= 1
        return 'питание'

    def work(self):
        self.satiety -= 1
        self.home.money += 2  # Они работают в IT
        return 'работа'

    def pay_meal(self):
        self.home.money -= 1
        self.home.meal += 1
        return 'закупка'

    def is_died(self):
        if self.satiety <= 0:
            return True
        return False

    def life_one_day(self):
        if self.is_died():
            return '___✝___'
        num = random.randint(1, 6)
        if self.satiety < 20 and self.home.meal >= 1:
            act = self.eat()
        elif self.home.meal < 10 and self.home.money >= 1:
            act = self.pay_meal()
        elif self.home.money < 50 and self.satiety >= 1:
            act = self.work()
        elif num == 1 and self.satiety >= 1:
            act = self.work()
        elif num == 2 and self.home.meal >= 1:
            act = self.eat()
        else:
            act = self.game()
        return act


class Home:
    def __init__(self, address='', meal=50, money=0):
        self.address = address
        self.meal = meal
        self.money = money


sasha = Human('Саша', Home('Ленина 111б'))             # Я думал адресс поможет объединению домов жильцов
masha = Human('Маша', sasha.home)                      # Но получилось только так
print(' День  Еды  Денег  Саша  Маша Дело Саши Дело Маши')
for day in range(1, 366):
    print('{:^6}{:^6}{:^6}{:^6}{:^6}{:^10}{:^10}'.format(
        day, sasha.home.meal, sasha.home.money, sasha.satiety, masha.satiety,
        sasha.life_one_day(), masha.life_one_day()
    ))
