import random


cont = 0
list = ''
listg = ''

while True:
    pc = random.randint(1, 11)
    print("""pair or odd?
    
    [0] = PAIR
    [1] = ODD
    
    """)
    choice = int(input('Your choice: '))
    n = int(input('type it a integer number: '))

    if choice ==  0:
        list = 'PAIR'
    elif choice == 1:
        list = 'ODD'

    play = n + pc

    if play % 2 == 0:
        listg = 'PAIR'
    else:
        listg = 'ODD'

    if list == listg:
        print('Player win!!!')
        cont += 1
    else:
        print('pc win!!!')
        break
print(f'You won {cont} times')
print('END')


