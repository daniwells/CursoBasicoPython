#pessoas = {'NOME':'Daniel', 'SEXO':'Masculino', 'IDADE':'18'}

#print(pessoas)
#print(pessoas['NOME'])
#print(f'The {pessoas["NOME"]} has {pessoas["IDADE"]} years')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

###########################################################################

"""for k in pessoas.keys():
    print(k)
"""
"""for k,v in pessoas.items():
    print(f'{k} = {v}')
"""

###########################################################################

#del pessoas['NOME']
#pessoas['NOME'] = 'Marcelo'
#print(pessoas['NOME'])
#pessoas['PESO'] = 77.4
#print(pessoas)

###########################################################################

"""
Brasil = []

estado = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}

Brasil.append(estado)
Brasil.append(estado2)

print(Brasil)
print(Brasil[0])
print(Brasil[1]['sigla'])
"""

###########################################################################
"""
estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = input('Federative unit: ')
    estado['sigla'] = input('Tthe abbreviation of state: ')
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'The camp {k} has value {v}')
"""
