from time import sleep

def tittle(txt):
    print('-' * (len(txt) + 5))
    print(f'{txt:^{len(txt) + 5}}')
    print('-' * (len(txt) + 5))

def hel(f):
    while True:
        print('\033[42m')
        tittle('SYSTEM OF HELP')
        print('\033[m')

        fun = input(f)

        if fun == 'stop':
            break

        print('\033[44m')
        tittle(f"Accessing the '{fun}' manual...")
        print('\033[m')
        sleep(1)

        print('\033[7;40m')
        help(fun)
        print('\033[m')

    sleep(0.5)
    print('\033[41m')
    tittle('Goodbye')
    print('\033[m')




funct = hel('Type it a function("stop" = end): ')