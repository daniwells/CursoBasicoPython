s = 0
list = []


for c in range(1, 7):
    n = int(input('type it the {}° number: '.format(c)))
    if n % 2 == 0:
        s = s + n
print('The sum of pair numbers is: {}'.format(s))



