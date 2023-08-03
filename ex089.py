listao = []
alu = []
nt = []
#cont = 0

while True:
    n = input('Name: ')
    nt1 = float(input('Note one: '))
    nt2 = float(input('Note two: '))

    #cont += 1

    nt.append(nt1)
    nt.append(nt2)
    #print(nt)

    alu.append(n)
    alu.append(nt[:])
    #print(alu)

    listao.append(alu[:])
    #print(listao)
    nt.clear()
    alu.clear()

    c = input('Do you want continue?(Y, N): ')
    c = c.upper()

    while c != 'Y' and c != 'N':
        c = input('Please, type it "Y" or "N": ').upper()

    if c == 'N':
        break
print('-=-==-=-=-=-=-=-=--=-==-=-=-=-=-=-=--=-==-=-=-=-=-=-=--=-==-=-=-=-=-=-=-')
print(f'{"ID":^5}', end=' ')
print(f'{"NAME":^5}', end='  ')
print(f'{"AVERAGE":^5}', end=' ')
print('\n')

for pos, num in enumerate(listao):
    print(f'{pos:^5}  {num[0]:^5}', end=' ')

    med = (num[1][0] + num[1][1]) / 2
    print('  {:.1f}'.format(med), end='')
    print('\n')
print('-=-==-=-=-=-=-=-=--=-==-=-=-=-=-=-=--=-==-=-=-=-=-=-=--=-==-=-=-=-=-=-=-')

p = 0
while p != 999:
    p = int(input('Show at the note which student: '))
    for pos, num in enumerate(listao):
        if pos == p:
            print(f'The notes of {num[0]} are {num[1]}')
    print('---------------------------------------------------')
print('END')