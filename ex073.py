tupla = ('Botafogo', 'Palmeiras', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Fluminense', 'Athletico-PR', 'São Paulo',
         'Fortaleza', 'Cruzeiro', 'Bragantino', 'Santos', 'Internacional', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás',
         'América-MG', 'Vasco da Gama', 'Coritiba')

print(f'The first five are: {tupla[0:5]}')
print(f'The last four are: {tupla[-1:-5:-1]}')
print(f'alphabetical order: {sorted(tupla)}')
print(f' The Fluminense is in {tupla.index("Fluminense") + 1}°  position')

