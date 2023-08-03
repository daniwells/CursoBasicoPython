list = []
cont = 0
lw = []
liwo = []

while True:
    name = input('Name: ')
    sex = input('Sex(M/F): ').upper()
    while sex != 'M' and sex != 'F':
        sex = input('Please, type it "M" or "F": ').upper()

    age = int(input('Age: '))

    dic = {
        'name':name,
        'sex':sex,
        'age':age
    }
    list.append(dic.copy())
    dic.clear()

    if sex == 'F':
        lw.append(name)
        lw.append(sex)
        lw.append(age)
        liwo.append(lw[:])
        lw.clear()

    cont += 1

    con = input('Do you want continue? (Y or N): ').upper()

    while con != 'Y' and con != 'N':
        con = input('Please, type it "Y" or "N": ').upper()

    if con == 'N':
        break

print('-=' * 30)
print(f'The group has {cont} people.')
sum = 0
for c in list:
    sum = sum + c['age']

med = sum // cont
print(f'The average of group is {med}.')
print(f'The women in the group are: ', end='')
for w in liwo:
    print(f'{w[0]}', end=' ')
print()
print(f'\nThe list of people with age greater than {med} are:')
mm = []
for c in list:
    if c['age'] > med:
        mm.append(c)

for e in mm:
    print(e)
    print()

print('END')