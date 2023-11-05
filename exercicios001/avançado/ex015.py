n1 = int(input('type it a integer number: '))
list = []

for num in range(1, n1 + 1):
    dv = n1 % num
    list.append(dv)

p = list.count(0)

if p == 2:
    print('This number is a prime number.')
else:
    print("This number don't is prime")