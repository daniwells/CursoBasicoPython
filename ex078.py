values = []


for c in range(0, 5):
    values.append(int(input('Type it a value: ')))
values2 = values[:]
print(f'The highest value is {max(values)} in position {values.index(max(values))}°', end=' ')

ma = max(values)
values.remove(max(values))
z = 0
while True:
    if max(values) == ma:
        x = z + values.index(max(values)) + 1
        print(f'{x}°')
        values.remove(max(values))
        z += 1
    else:
        break

print(f'\nThe lower value is {min(values2)} in position {values2.index(min(values2))}°', end=' ')

mi = min(values2)
values2.remove(min(values2))
w = 0

while True:
    if min(values2) == mi:
        y = w + values2.index(min(values2)) + 1
        print(f'{y}°')
        values2.remove(min(values2))
        w += 1
    else:
        break

#####################################################################################






