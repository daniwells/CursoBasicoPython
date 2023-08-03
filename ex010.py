n1 = float(input('type it your amount money in real:'))
result = n1 / 3.27

color = {'clean': '\033[m', 'azul':'\033[4;34m'}

print('witch that money you can buy {}{}{} dollars'.format(color['azul'], result, color['clean']))
