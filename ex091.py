from random import randint
from time import sleep
from operator import itemgetter

list = [{'player':'player 1', 'value': 0}, {'player':'player 2', 'value': 0}, {'player':'player 3', 'value': 0},
        {'player':'player 4', 'value': 0}]

list[0]['value'] = randint(1, 6)
list[1]['value'] = randint(1, 6)
list[2]['value'] = randint(1, 6)
list[3]['value'] = randint(1, 6)

print(f'{"Values sorted:":^5}')
for c in list:
    print(f'The {c["player"]} rolled {c["value"]}')
    sleep(0.5)
mai = 0
nm = ''
n = ''
cont = 0

print('-=' * 30)

print(f'   = {"Player Ranking":^5} =')
while cont < 4:
    cont += 1
    for c in list:
        if mai == 0:
            mai = list[0]['value']
            nm = 0
            n = c['player']
        elif c['value'] > mai:
            mai = c['value']
            nm = list.index(c)
            n = c['player']
    print(f'The {cont}º is {n} with {mai}')
    sleep(0.5)
    del list[nm]
    mai = 0

################################################################################################
"""
dic = {
    'player 1':randint(1, 6),
    'player 2':randint(1, 6),
    'player 3':randint(1, 6),
    'player 4':randint(1, 6)
}
print(dic)
r = sorted(dic.items(), key=itemgetter(1))
print(r)"""