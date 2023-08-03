listao = []
list1 = []
list2 = []
list3 = []
cont = 0
sp = 0

for c in range(0, 9):
    n = int(input(f'Type it a number for the position {c + 1}º: '))
    cont += 1
    if cont < 4:
        list1.append(n)
    elif 3 < cont < 7:
        list2.append(n)
    elif 6 < cont < 10:
        list3.append(n)

    if n % 2 == 0:
        sp = sp + n

listao.append(list1)
listao.append(list2)
listao.append(list3)

print('MATRIZ: ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

"""
print(f'[ {listao[0][0]} ] [ {listao[0][1]} ] [ {listao[0][2]} ]')
print(f'[ {listao[1][0]} ] [ {listao[1][1]} ] [ {listao[1][2]} ]')
print(f'[ {listao[2][0]} ] [ {listao[2][1]} ] [ {listao[2][2]} ]')"""

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{listao[l][c]:^6}]', end='')
    print()

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print(f'The sum of all even numbers: {sp}')
s3 = listao[0][2] + listao[1][2] + listao[2][2]
print(f'The sum of third column: {s3}')
print(f'The greatest value of second line: {max(listao[1])}')

###################################################################################################
"""sp2 = 0
sc = 0
mai = 0

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{listao[l][c]:^6}]', end='')
        if listao[l][c] % 2 == 0:
            sp += listao[l][c]
    print()

for s in range(0, 3):
    sc += listao[s][2]

for m in range(0, 3):
    if mai == 0:
        mai = listao[1][m]
    elif listao[1][m] > mai:
        mai = listao[1][m]

print(sp2) #A soma dos valores pares
print(sc) #A soma de todos os valores da terceira coluna
print(mai) # O maior valor da segunda linha
"""
