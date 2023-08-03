#print('good \033[1;31mmorning!\033[m')

##########################################

#name = 'marcos'

#print('hello, very nice to meet you {}{}{}!'.format('\033[4;34m', name, '\033[m'))

##########################################

name = 'marcos'
colors = {'limpa':'\033[m', 'azul':'\033[3;34m'}

print('hello, very nice to meet you {}{}{}!'.format(colors['azul'], name, colors['limpa']))
