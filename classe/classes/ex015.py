from random import randint
from PACOTES import textos

class Animal:
    def __init__(self, name, hunger, tedium):
        self.name = name
        self.hunger = hunger
        self.tedium = tedium


class Farm:
    def __init__(self, animals):
        self.animals = animals
        self.animals2 = []
        for a in self.animals:
            ani = Animal(a, randint(1, 3), randint(1, 3))
            self.animals2.append(ani)

    def feed(self):
        for a in self.animals2:
            if a.hunger <= 2:
                a.hunger += 1

    def play(self):
        for a in self.animals2:
            if a.tedium <= 2:
                a.tedium += 1

    def show(self):
        textos.title('ANIMALS')
        h = ''
        t = ''
        for a in self.animals2:

            if a.hunger == 1:
                h = 'very hungry'
            elif a.hunger == 2:
                h = 'hungry'
            elif a.hunger == 3:
                h = 'no hungry'

            if a.tedium == 1:
                t = 'very bored'
            elif a.tedium == 2:
                t = 'bored'
            elif a.tedium == 3:
                t = 'happy'

            print('-' * 15)
            print(f'{a.name}:')
            print(f'HUNGER = {h}')
            print(f'TEDIUM = {t}')
            print('-' * 15)



list = ['pig', 'horse', 'chicken', 'dog', 'cow']

f = Farm(list)

f.show()

print('=-' * 30)

f.feed()

f.play()

f.show()
