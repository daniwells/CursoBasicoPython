n = int(input('Type it the value to be withdrawn: '))

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

if n >= 50:
    while True:
        n = n - 50
        c1 = n

        if c1 < 50:
            cont1 += 1
            break
        cont1 += 1
else:
    c1 = n

if c1 >= 20:
    while True:
        c1 = c1 - 20
        c2 = c1

        if c2 < 20:
            cont2 += 1
            break
        cont2 += 1

else:
    c2 = c1

if c2 >= 10:
    while True:
        c2 = c2 - 10
        c3 = c2
        if c3 < 10:
            cont3 += 1
            break
        cont3 += 1

else:
    c3 = c2

if c3 > 0:
    while True:
        c3 = c3 - 1
        c4 = c3

        if c4 < 1:
            cont4 += 1
            break
        cont4 += 1



print(f'it is {cont1} notes of 50')
print(f'it is {cont2} notes of 20')
print(f'it is {cont3} notes of 10')
print(f'it is {cont4} notes of 1')
