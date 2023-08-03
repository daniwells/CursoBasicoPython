def readInt(num):
    n = input(num)
    while n.isnumeric() is False:
        print('\033[1;31mType it a valid integer number!\033[m')
        n = input(f'{num}')
    return n

n = readInt('Type it a integer number: ')
print(f'You typed the value: \033[1;32m{n}\033[m')
