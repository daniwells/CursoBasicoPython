import random

n1 = random.randint(0, 10)
n2 = random.randint(0, 10)
n3 = random.randint(0, 10)
n4 = random.randint(0, 10)
n5 = random.randint(0, 10)

tupla = (n1, n2, n3, n4, n5)

print('The values assorted are:', end=' ')
for c in tupla:
    print(f'{c}', end=' ')

print(f'\nThe highest value is: {max(tupla)}')
print(f'The lower value is: {min(tupla)}')
