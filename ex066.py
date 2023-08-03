n2 = 0
cont = 0


while True:
    n = int(input('type it a integer value: '))
    if n == 999:
        break
    n2 = n2 + n
    cont += 1
print(f'{cont}')
print(f'{n2}')
