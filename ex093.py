lg = []
dic = {}

name = input('Name of Player: ')
ng = int(input('Number of games: '))

for c in range(0, ng):
    g = int(input(f'which much gols in the game {c}: '))
    lg.append(g)

dic['name'] = name
dic['goals'] = lg
dic['total'] = sum(lg)
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