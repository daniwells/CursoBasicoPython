print('{:=^40}'.format(" DANIEL'S STORE "))

vi = float(input('type it the price of product: '))

print("""type it the form of payment.
    [1] "money/check". 
    [2] the view on the card. 
    [3] 2x on the card and.
    [4] 3x or more on the card.""")

pag = input('Your choice: ')

if pag == '1' or pag == '2' or pag == '3' or pag == '4':
    if pag == '1':
        p = vi * 0.1
        print('The final price is: {}'.format(vi - p))
    elif pag == '2':
        p = vi * 0.05
        print('The final price is: {}'.format(vi - p))
    elif pag == '3':
        pa = vi / 2
        print('The final price is: {}'.format(vi))
        print('Will be {} for portion.'.format(p))
    elif pag == '4':
        pa = int(input('Type it the amount of portion:'))
        p = vi * 0.20
        print('The final price is: {}'.format(vi + p))
        print('Will be {} for portion.'.format((vi + p) / pa))
else:
    print('\033[4;31mtype it a valid value!!\033[m')
    exit()



