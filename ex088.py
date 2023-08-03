import random
listao = []
list = []

ng = int(input('type it the number of guess: '))

for c in range(0, ng):
    for b in range(0, 7):
        na = random.randint(1, 61)
        if na not in list:
            list.append(na)
    listao.append(list[:])
    list.clear()

cont = 0
for c in listao:
    cont += 1
    print(f'Game {cont}:{c}')