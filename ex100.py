import random

def sor(lst):
    for c in range(0, 5):
        lst.append(random.randint(0, 11))
    print(f'The sorted values are \033[32m{lst}\033[m', end=' ')

list = []
sor(list)

def sp(p):
    pair = []
    for e in p:
        if e % 2 == 0:
            pair.append(e)
    print(f'and the sum of pair values is \033[32m{sum(pair)}\033[m', end='')

sp(list)