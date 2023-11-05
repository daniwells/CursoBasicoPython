from PACOTES import textos

class Monkey:
    def __init__(self, name):
        self.name = name
        self.stomach = []

    def eat(self, *food):
        for i in food:
            self.stomach.append(i)

    def show_stomach(self):
        print(f'In the stomach of mokey has: ',  end='')
        for i in self.stomach:
             print(f'{i} ', end='')
        print('\n')

    def digest(self, food_st):
        for e in self.stomach:
            if food_st in e:
                del self.stomach[self.stomach.index(e)][e.index(food_st)]
            else:
                print(f"The monkey didn't eat {e}")

monk1 = input('Enter a name for the monkey: ')
n = Monkey(monk1)

print()

print(f'The first monkey is {n.name}')

monk2 = input('Enter a name of second monkey')
n2 = Monkey(monk2)

list = [monk1, monk2]

m = monk1

while True:

    textos.title('Eating a Monkey!')

    print('-=' * 15)
    print(f"""   
[1] Give food for the monkey.

[2] See stomach of monkey.

[3] Do the monkey digest the foods.

[4] To replace monkey.
    """)
    print('-=' * 15)
    print()

    try:
        e = int(input('Your choice: '))
    except:
        print('ERROR! Enter a correct value.')
        continue
    else:

        if e == 1:
            num_eat = int(input('Enter a number of foods that monkey go eating: '))
            foods = []
            print()

            for c in range(0, num_eat):
                f = input('Enter a food:')
                foods.append(f)

            n.eat(foods)



        elif e == 2:
            textos.title('Stomach Of Monkey')
            n.show_stomach()

        elif e == 3:
            print('-' * 15)
            n.show_stomach()
            print('-' * 15)
            print()

            if len(n.stomach) == 0:
                print("The monkey don't has any for digest!")
                continue
            else:
                d = input('Which food do you want digest? ')

                for e in n.stomach:
                    if d in e:
                        n.digest(d)

        elif e == 4:
            print('Wihch monkey do you to feed')
            print(f"""
1 - {n.name}

2 - {n2.name}
""")

            ch = int(input('Your choice: '))
            if ch == 1:
                m = n
            elif ch == 2:
                m = n2
            else:
                print("This monkey don't exist!")
                continue

        else:
            print('ERROR! Enter a valid option.')
            continue

