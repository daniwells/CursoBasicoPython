class Tamagushi:
    def __init__(self, name, hunger, health, age):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.age = age
        self.humor = 'happy'
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
            else:
                print('This value does not exist')

    def mor(self):

        h = 0

        if self.hunger == 'no hungry':
            h = 10
        elif self.hunger == 'hungry':
            h = 6
        elif self.hunger == 'very hungry':
            h = 1

        hu = (h + self.health) / 2

        if hu >= 8:
            self.humor = 'happy'
        elif 6 <= hu < 8:
            self.humor = 'bored'
        elif hu < 6:
            self.humor = 'very sad'

tama = Tamagushi('Ronaldo', 'no hungry', 2, 4)

tama.change(name='Rogério', hunger = 'hungry')

print(tama.name)
print(tama.hunger)

tama.show('fadgfd', 'name', 234234, 'age')

tama.mor()

print(tama.humor)