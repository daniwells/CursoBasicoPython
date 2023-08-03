n1 = int(input('type it a number: '))

list = []
for c in range(1, n1 + 1):
    p = n1 % c
    list.append(p)
    if p == 0:
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}\033[m'.format(c), end=' ')

q = list.count(0)

if q == 2:
    print('\nthis number is a prime number.')
else:
    print('\nthis number is not a prime number')

