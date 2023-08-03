p = float(input('Type it your weight:(Kg)'))
h = float(input('Type it your height(m):'))

imc = p / (h ** 2)

if imc < 18.5:
    print('Under weight.')
elif 18.5 >= imc <= 25:
    print('between the weight.')
elif 25 > imc <= 30:
    print('about the weight.')
elif 30 > imc <= 40:
    print('obesity.')
elif imc > 40:
    print('morbid obesity')


