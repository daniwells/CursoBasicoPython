values = []
last = '0'

while True:
    n = (int(input('type it a value: ')))
    if n in values:
        print('This value is duplicate, cant be added')
    else:
        values.append(n)
    p = input('Do you want continue?(Y/N): ')
    p = p.upper()
    while p != 'Y' and p != 'N':
        p = input('Please type it \033[31m"Y"(YES)\033[m or \033[31m"N"(NO)\033[m: ')
        p = p.upper()
    if p == 'N':
        break

values.sort()
for v in values:
    print('the values in order are:')
    print(f'\033[33m{v}\033[m', end=' ')
