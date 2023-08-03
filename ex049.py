n1 = int(input('type it a number: '))

print('the multiplication table this number is:')

for c in range(1, 11):
    print(n1, 'x', c, '= {}'.format(c * n1))