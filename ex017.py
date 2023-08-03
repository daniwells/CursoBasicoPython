co = float(input('type it opposite leg of triangle:'))
ca = float(input('type it adjacent leg of triangle:'))

h2 = (co ** 2) + (ca ** 2)

h = h2 ** (1/2)

print('The hypotenuse of this triangle is: {:.2}'.format(h))