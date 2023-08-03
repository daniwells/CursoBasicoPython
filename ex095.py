from operator import itemgetter

listao = []
lg = []
dic = {}

while True:
    name = input('Name of Player: ')
    ng = int(input('Number of games: '))

    for c in range(0, ng):
        g = int(input(f'which much gols in the game {c}: '))
        lg.append(g)

    dic['name'] = name
    dic['goals'] = lg[:]
    dic['total'] = sum(lg)
    lg.clear()


    listao.append(dic.copy())
    dic.clear()

    con = input('Do you want continue?(Y/N): ').upper()

    while con != 'Y' and con != 'N':
        con = input('please, type it "Y" or "N": ').upper()

    if con == 'N':
        break

print(listao)
print('-=' * 30)
print(f'{"ID":^10}{"NAME":^10}{"GOALS":^20}{"TOTAL":^10}', end=' ')


sort = sorted(listao, key=lambda dic: dic['total'], reverse=True)
print('\n')
cont = -1
for e in sort:
    cont += 1
    print(f'{cont:^10}', end='')
    print(f'{e["name"]:^10}', end=' ')
    print(f'{str(e["goals"]):^20}', end=' ')
    print(f'{e["total"]:^10}', end=' ')
    print()

conti = 0
cont2 = 0

print('-=' * 30)
while True:
    conti = int(input('Do you know to see the data of which player?(999 = stop): '))

    if conti == 999:
        break

    if conti >= len(sort):
        print('ERROR! This id is not in the list.')
    else:
        for el in sort[conti]['goals']:
            cont2 += 1
            print(f'In the game {cont2} scored {el} goals')

"""
print('-=' * 30)
for k, v in dic.items():
    print(f'The {k} has the value {v}')
print('-=' * 30)

cont = 0
print(f'The player {dic["name"]} played {ng} games.')
for c in lg:
    cont += 1
    print(f'In the game {cont}, he did {c} goals')
print(f'It was a total of {dic["total"]} goals')
"""