tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Type it a number between 0 to 20: '))
while n < 0 or n > 20:
    n = int(input('Please, type it a number between 0 to 20: '))

print(f'This number in extensive is \033[4m{tupla[n]}')