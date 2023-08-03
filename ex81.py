list = []
cont = 0
while True:
    n = int(input('type it a number: '))
    list.append(n)

    cont += 1

    conti = input('Do you want continue?(Y = yes /N = no): ')
    conti = conti.upper()

    while conti != 'Y' and conti != 'N':
        conti = input('Please, type it "Y" or "N"!!').upper()

    if conti == 'N':
        break

print(f'The values typed were: {list}')
print(f'the amount of numbers typed are: {cont}')
if 5 in list:
    print('Value 5 is in the list')
    print(f'The position of value 5 is: {list.index(5)}')
else:
    print('Value 5 was not typed and is not in the list')

list.sort(reverse=True)
print(f'The list in reverse order if: {list}')
