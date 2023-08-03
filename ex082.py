list = []
p = []
i = []

while True:
    n = int(input('Type it a number: '))
    list.append(n)

    c = input('Do you want continue?(Y/N): ')
    c = c.upper()

    while c != 'Y' and c != 'N':
        c = input('Please, type it "Y" or "N": ').upper()

    if c == 'N':
        break

for c in list:
    if c % 2 == 0:
        p.append(c)
    else:
        i.append(c)

print(f'The numbers of typed were: {list}')
print(f'The pair numbers of typed were: {p}')
print(f'the odd numbers of typed were: {i}')