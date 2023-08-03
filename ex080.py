values = []
vd = []

ns = int(input('type it a value: '))
values.append(ns)

ns2 = int(input('type it a value: '))
if ns2 in values:
    values.insert(values.index(ns2), ns2)
    print(values.index(ns2))
elif ns2 < values[0]:
    values.insert(0, ns2)
else:
    values.append(ns2)


n = int(input('type it a value: '))
if n in values:
    values.insert(values.index(n), n)
elif n < values[0]:
    values.insert(0, n)
elif values[0] < n < values[1]:
    values.insert(1, n)
else:
    values.append(n)


n2 = int(input('type it a value: '))

if n2 in values:
    values.insert(values.index(n2), n2)
elif n2 > values[2]:
    values.append(n2)
else:
    if n2 > values[1]:
        values.insert(2, n2)
    elif values[0] < n2 < values[1]:
        values.insert(1, n2)
    elif n2 < values[0]:
        values.insert(0, n2)


n3 = int(input('type it a value: '))

if n3 in values:
    values.insert(values.index(n3), n3)
elif n3 > values[3]:
    values.append(n3)
else:
    if n3 > values[2]:
        values.insert(3, n3)
    elif values[1] < n3 < values[2]:
        values.insert(2, n3)
    elif values[0] < n3 < values[1]:
        values.insert(1, n3)
    elif n3 < values[0]:
        values.insert(0, n3)

print(f'The typed values are: {values}')

