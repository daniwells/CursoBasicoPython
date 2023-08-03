cont = 0
cont2 = 0
cont3 = 0
choice = 1

while True:
    age = int(input('Type it the age: '))
    print("""
    [1] = MASCULINE
    [0] = FEMININE 
    """)

    sex = int(input('type it the sex: '))

    while sex > 1 or sex < 0:
        sex = int(input('type it the sex(1, 0): '))

    if age >= 18:
        cont += 1
    if sex == 1:
        cont2 += 1
    if sex == 0:
        if age < 20:
            cont3 += 1

    print("""Do you want continue?
    
    [1] = "YES"
    [0] = "NO"
    
    """)

    choice = int(input(': '))

    while choice > 1 or choice < 0:
        choice = int(input('(0, 1): '))

    if choice == 0:
        break

if sex == 0 or sex == 1 and choice == 0 or choice == 1:
    print(f'There are {cont} people with age greater than 18.')
    print(f'There are {cont2} men.')
    print(f'There are {cont3} women with age less than 20.')
print('END')



