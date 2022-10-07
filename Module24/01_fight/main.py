import random


class Fighter:
    def __init__(self, name='nobody', health=100, power=20):
        self.health = health
        self.name = name
        self.power = power

    def punch(self, people):
        if people.health > self.power:
            people.health -= self.power
        else:
            people.health = 0
        print('{0} punch {1}. {1} has {2} health.'.format(
            self.name, people.name, people.health))

    def is_dead(self):
        if self.health == 0:
            return True
        return False

    def winner(self):
        print('{} wins with health: {}.'.format(self.name, self.health))


fst_fighter = Fighter('Stefan', 79, 22)
sec_fighter = Fighter('Efraim', 109, 18)
while not (fst_fighter.is_dead() or sec_fighter.is_dead()):
    if random.randint(0, 1):
        fst_fighter.punch(sec_fighter)
    else:
        sec_fighter.punch(fst_fighter)

if fst_fighter.is_dead():
    sec_fighter.winner()
else:
    fst_fighter.winner()
