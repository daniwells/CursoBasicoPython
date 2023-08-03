listao = []
p = []
qcont = 0

while True:
    name = input('Name: ')

    while name.isalpha() is False:
        name = input('Please, type it the corrector characters: ')
    p.append(name)

    w = float(input('Weight: '))
    p.append(w)

    listao.append(p[:])
    p.clear()
    qcont += 1

    conti = input('Do you want continue?(Y, N)')
    conti = conti.upper()

    while conti != 'Y' and conti != 'N':
        conti = input('Please, type it "Y" or "N"').upper()

    if conti == 'N':
        break

print(f'The amount of data registred are: {qcont}')

ma = []
for m in listao:
    if m[1]:
        ma.append(m[1])
ma.sort()

print(f'The heaviest person is/are: ', end=' ')
for c in listao:
    if c[1] == ma[-1]:
        print(f'[\033[1;34m{c[0]}\033[m]', end=' ')

print('with: ', end='')
print()
print(f'\033[1;34m{ma[1]}\033[m')

print(f'The lighter people are/is: ', end=' ')
for c in listao:
    if c[1] == ma[0]:
        print(f'[\033[1;34m{c[0]}\033[m]', end=' ')

print()

print('with: ', end='')
print(f'\033[1;34m{ma[0]}\033[m', end=' ')

#########################################################################################

"""
listao = []
p = []
qcont = 0
mai = 0
men = 0

while True:
    name = input('Name: ')

    while name.isalpha() is False:
        name = input('Please, type it the corrector characters: ')
    p.append(name)

    w = float(input('Weight: '))
    p.append(w)

    if len(listao) == 0:
        mai = p[1]
        men = p[1]
    else:
        if p[1] > mai:
            mai = p[1]
        if p[1] < men:
            men = p[1]

    listao.append(p[:])
    p.clear()
    qcont += 1

    conti = input('Do you want continue?(Y, N)')
    conti = conti.upper()

    while conti != 'Y' and conti != 'N':
        conti = input('Please, type it "Y" or "N"').upper()

    if conti == 'N':
        break
print(qcont)
print(mai)
print(men)
"""
