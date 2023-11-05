from PACOTES import textos
class Tamagushi:
    def __init__(self, name):
        self.name = name
        self.hunger = 'no hungry'

        self.health = 10
        self.age = 1
        self.humor = 'happy'

        self.h = 10
    def change(self, name=0, hunger=0, health=0, age=0):
        list = [name, hunger, health, age]
        cont = 0
        for e in list:
            cont = cont + 1
            if e != 0:
                if cont == 1:
                    self.name = name
                elif cont == 2:
                    self.hunger = hunger
                    if self.hunger == 'no hungry':
                        self.h = 10
                    elif self.hunger == 'hungry':
                        self.h = 6
                    elif self.hunger == 'very hungry':
                        self.h = 0
                elif cont == 3:
                    self.health = health
                elif cont == 4:
                    self.age = age
    def show(self, *atr):
        for e in atr:
            if e == 'name':
                print(self.name)
            elif e == 'hunger':
                print(self.hunger)
            elif e == 'health':
                print(self.health)
            elif e == 'age':
                print(self.age)
            elif e == 'humor':
                print(self.humor)
            else:
                if e == 'senha':
                    textos.title('VALUES OF ATTRIBUTES')
                    print(f' NAME: {self.name}')
                    print(f' HUNGER: {self.hunger}')
                    print(f' HUNGER IN NUMBER: {self.h}')
                    print(f' HEALTH: {self.health}')
                    print(f' AGE: {self.age}')
                    print(f' HUMOR: {self.humor}')
                else:
                    print('This value does not exist')



    def mor(self):

        if self.hunger == 'no hungry':
            self.h = 10
        elif self.hunger == 'hungry':
            self.h = 6
        elif self.hunger == 'very hungry':
            self.h = 0

        hu = (self.h + self.health) / 2

        if hu >= 7:
            self.humor = 'happy'
        elif 5 <= hu < 7:
            self.humor = 'bored'
        elif hu < 5:
            self.humor = 'very sad'

    def feed(self, amount_food):
        if 10 >= amount_food >= 0:
            self.h = amount_food

            if self.h < 5:
                self.hunger = 'very hungry'
            if 5 <= self.h <= 6:
                self.hunger = 'hungry'
            if 6 < self.h <= 10:
                self.hunger = 'no hungry'

    def play(self, time_play):
        if 10 >= time_play >= 0:
            self.health = time_play

tama = Tamagushi('Ronaldo')

tama.change(name='Rogério', hunger = 'hungry')

print(tama.name)
print(tama.hunger)

tama.show('fadgfd', 'name', 234234, 'age')

tama.mor()

print(tama.humor)

print('=-' * 30)

tama2 = Tamagushi('Marcelo')

tama2.feed(6)
tama2.play(4)

tama2.mor()

tama2.show('humor')

tama2.show('senha')