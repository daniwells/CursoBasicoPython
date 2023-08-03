"""teste = list()
teste.append('gustavo')
teste.append(48)

galera = list()
galera.append(teste[:])

teste[0] = 'João'
teste[1] = '40'

galera.append(teste[:])

# uma cópia deve ser criada, pois quando se iguala uma lista uma ligação é criada.

print(galera)"""

############################################################

"""
listao = [['Juliana', 43], ['Marcos', 19], ['Diogo', 15]]
print(listao)
print(listao[0])
print(listao[0][0])
print(listao[2][1])

for c in listao:
    #print(c)
    print(c[0])
    print(c[1])
"""

############################################################

listao = list()
dados = list()
cont = 0
for c in range(0, 4):
    dados.append(input('name: '))
    dados.append(int(input('age: ')))
    listao.append(dados[:])
    dados.clear()

for p in listao:
    if p[1] > 21:
        print(f'{p[0]} have age greater than twenty-one!')
        cont += 1

print(f'Are {cont} peoples whith age greater than twenty-one')
#print(listao)
