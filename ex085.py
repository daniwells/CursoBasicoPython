"""listao = []
pair = []
odd = []

for c in range(0, 6):
    n = int(input('Type it a number: '))
    if n % 2 == 0:
        pair.append(n)
    else:
        odd.append(n)

listao.append(pair[:])
listao.append(odd[:])

listao[0].sort()
print(f'The pair values typed are: {listao[0]}')
listao[1].sort()
print(f'The odd values typed are: {listao[1]}')"""

##############################################################################################

listao = [[], []]

for c in range(0, 6):
    n = int(input('Type it a number: '))
    if n % 2 == 0:
        listao[0].append(n)
    else:
        listao[1].append(n)

listao[0].sort()
print(f'The pair values typed are: {listao[0]}')
listao[1].sort()
print(f'The odd values typed are: {listao[1]}')