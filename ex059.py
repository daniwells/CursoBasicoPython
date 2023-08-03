from time import sleep

menu = 1

n1 = int(input('type it the first number: '))

n2 = int(input('type it the second number: '))

while menu != 5:
    sleep(0.5)
    print("""------ MENU ------
    
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR VALOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
    
    """)
    menu = int(input('type it your choice: '))

    if menu == 1:
        print('the sum of the two values is {}'.format(n1 + n2))
    elif menu == 2:
        print('the multiplication of thw two values is {}'.format(n1 * n2))
    elif menu == 3:
        if n1 < n2:
            print('The greatest value is {}'.format(n2))
        else:
            print('The greatest value is {}'.format(n1))
    elif menu == 4:
        print('------ type it new values ------')
        n1 = int(input('type it the first value: '))
        n2 = int(input('type it the second value: '))
print('END')