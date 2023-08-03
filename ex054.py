import datetime

dma = []
dme = []

for c in range(1, 8):
    yob = int(input('Type it your year of birth: '))
    age = datetime.date.today().year - yob
    if age >= 18:
        dma.append(age)
    else:
        dme.append(age)

print('{} reached the age of majority'.format(len(dma)))
print('{} not reached the age of majority'.format(len(dme)))


