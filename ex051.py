n1 = int(input('Type it the first number of arithmetic progression: '))
n2 = int(input('Type it the reason of arithmetic progression: '))

print('{:=^100}'.format(' The Arithmetic Progression '))
print(n1, end=' ')
for c in range(1, 10):
    n1 = n1 + n2
    print(n1, end=' ')
