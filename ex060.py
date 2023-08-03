n = int(input('type it a value: '))

c = n - 1

print('{} x {} '.format(n, c), end='')

while c != 1:
    n = n * c
    c = c - 1
    print('x {} '.format(c), end='')
    #list.append(c)
#print(list)
print('\nThe result is {}'.format(n))
