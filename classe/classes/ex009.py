from PACOTES import textos

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_point(self):
        print(f'X = {self.x}')
        print(f'Y = {self.y}')

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def center_retangle(self):
        x = self.width / 2
        y = self.height / 2

        return x, y

while True:

    textos.title('Rectangle Dimensions')

    w = float(input('Enter the width of rectangle: '))
    h = float(input('Enter the height of rectangle: '))

    rect1 = rectangle(width=w, height=h)

    textos.title('Rectangle Center: ')

    p = rect1.center_retangle()

    po1 = point(p[0], p[1])
    print('-' * 15)
    po1.show_point()
    print('-' * 15)

    conti = input('Do you want to change the values of rectangle?(Y, N): ').upper()

    while conti != 'Y' and conti != 'N':
        conti = input('Please, Enter "Y" or "N": ').upper()

    if conti == 'Y':
        continue
    else:
        break

print('END')


