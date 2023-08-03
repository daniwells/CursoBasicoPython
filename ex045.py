import random
from time import sleep

p = input('type it "PEDRA", "PAPEL" or "TESOURA":')

print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO')

p = p.upper()

list = ['PEDRA', 'PAPEL', 'TESOURA']

pc = random.choice(list)

if p == 'PEDRA' or p == 'PAPEL' or p == 'TESOURA':
    print('pc: {}'.format(pc))
    print('player: {}'.format(p))
    if p == pc:
        print('The game impacted')
    elif pc == 'PEDRA' and p == 'PAPEL':
        print('Player win')
    elif pc == 'PAPEL' and p == 'PEDRA':
        print('PC win')
    elif pc == 'TESOURA' and p == 'PEDRA':
        print('Player win')
    elif pc == 'PEDRA' and p == 'TESOURA':
        print('PC win')
    elif pc == 'PAPEL' and p == 'TESOURA':
        print('Player win')
    elif pc == 'TESOURA' and p == 'PAPEL':
        print('PC win')
else:
    print('Invalid text!!!')
