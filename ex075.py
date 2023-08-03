n1 = int(input('Type it the first value: '))
n2 = int(input('Type it the second value: '))
n3 = int(input('Type it the third value: '))
n4 = int(input('Type it the fourth value: '))

tupla = (n1, n2, n3, n4)

print(f'The values entered are: {tupla}')

print(f'The amount of value "9" in list is {tupla.count(9)}')

if 3 in tupla:
    print(f'The position of value "3" in list is {tupla.index(3)}')
else:
    print('There not the value "3" in list')

print('The pair values in list are:', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(f'{c}', end=' ')