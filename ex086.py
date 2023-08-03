"""listao = []
list1 = []
list2 = []
list3 = []
cont = 0

for c in range(0, 9):
    n = int(input(f'Type it a number for the position {c + 1}º : '))
    cont += 1
    if cont < 4:
        list1.append(n)
    elif 3 < cont < 7:
        list2.append(n)
    elif 6 < cont < 10:
        list3.append(n)

    #print(cont)
    #print(list1, list2, list3)

listao.append(list1)
listao.append(list2)
listao.append(list3)

print(f'[   {listao[0][0]}   ] [   {listao[0][1]}   ] [   {listao[0][2]}   ]')
print(f'[   {listao[1][0]}   ] [   {listao[1][1]}   ] [   {listao[1][2]}   ]')
print(f'[   {listao[2][0]}   ] [   {listao[2][1]}   ] [   {listao[2][2]}   ]')"""

#################################################################################################

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'type it a value for the [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()