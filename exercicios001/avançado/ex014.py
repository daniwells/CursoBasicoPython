import random
from pacote import string
from pacote import numero

string.title('Game of Divination')

pont = 0
pt = 0

cont = 0
pc = random.randint(0, 11)

while True:
    while True:
        cont += 1
        play = numero.error('Guess the number(between 0 to 10): ')
        if play == pc:
            if cont == 1:
                pont = 100
            elif cont == 2:
                pont = 70
            elif cont == 3:
                pont = 35
            elif cont == 4:
                pont = 20
            elif cont == 5:
                pont = 10

            pt = pt + pont
            print(f'Do you win!!! Do you make \033[1;31m{pont}pts.\033[m Your score now is: \033[1;31m{pt}pts\033[m')
            break
        if cont == 5:
            print('Do you lost!!!')
            break
    pont = 0
    cont = 0
    print(f'The number was \033[1;32m{pc}.\033[m')
    print()

    c = input('Do you want continue?(Y=yes or N=no): ').upper()
    while c != 'Y' and c != 'N':
        c = input('Please, type it "Y" or "N": ').upper()

    if c == 'N':
        print('Thanks for playing, come back always!')
        break


