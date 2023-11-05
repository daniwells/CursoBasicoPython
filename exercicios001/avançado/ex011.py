from pacote import string

gf = string.title('Celsius to Fahrenheit')

list = [22.5, 40, 13, 29, 34]

for e in list:
    result = (e * (9/5)) + 32
    print(f'Graus in Celsius: {e} -> in Fahrenheit: {result:.2f} ')
    print()
