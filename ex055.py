
list = []
for c in range(1, 6):
    p = float(input('type it the Weight(Kg) for {}° people: '.format(c)))
    list.append(p)
print('The smallest weight is {}'.format(min(list)))
print('The bigger weight is {}'.format(max(list)))