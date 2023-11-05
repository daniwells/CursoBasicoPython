def title(p):
    print('-' * (len(p) + 15))
    print(f'{p:^{len(p) + 15}}')
    print('-' * (len(p) + 15))

class people:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_old(self):
        if self.age < 21:
            self.age = self.age + 1
            self.height = self.height + 0.5
        else:
            self.age = self.age + 1

    def fatten(self):
        self.weight = self.weight + 0.5

    def lose_weight(self):
        self.weight = self.weight - 0.5

    def grow(self):
        self.height = self.height + 0.5


pe = people('Daniel', 18, 45, 165)

while True:

    title('People Class')
    print("""
    
[1] Get Old
[2] Fatten
[3] To Lose Weight
[4] To grow

    """)
    while True:
        try:
            choice = int(input('Enter your choice: '))
        except:
            print('ERROR! Enter a valid value.')
        else:
            if 5 > choice > 0:
                break
            print('ERROR! Enter a valid value.')


    if choice == 1:
        title('Get Old')
        year = int(input('How much does the get old will people?(IN YEARS): '))

        for c in range(0, year):
            pe.get_old()
        print(f'The people aged {pe.age}')

    elif choice == 2:
        title('Fatten')
        f = int(input('How much does the fatten will people?(IN KG): '))

        for c in range(0, f * 2):
            pe.fatten()
        print(f'The people has {pe.weight}Kg now.')

    elif choice == 3:
        title('To Lose Weight')
        f = int(input('How much weight will a person lose?(IN KG): '))

        for c in range(0, f * 2):
            pe.lose_weight()
        print(f'The people has {pe.weight}Kg now.')

    elif choice == 4:
        title('Grow')
        f = int(input('How much height will a person gain?(IN cm): '))

        for c in range(0, f * 2):
            pe.grow()
        print(f'The people has {pe.height}cm now.')



    cont = input('Do you want continue?(Y or N): ').upper()

    while cont != 'Y' and cont != 'N':
        cont = input("please, enter 'Y' or 'N'").upper()

    if cont == 'N':
        break
    else:
        continue

title('people')
print('-=' * 15)

print(f'Name: {pe.name}')
print(f'Age: {pe.age}')
print(f'weight: {pe.weight}')
print(f'Height: {pe.height}')

print('-=' * 15)

print('END')
