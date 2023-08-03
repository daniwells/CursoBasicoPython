nt1 = float(input('type it the your first note:'))
nt2 = float(input('type it the your second note:'))

if nt1 > 10.0:
    print('Please type it a valid note.')
    exit()
elif nt2 > 10.0:
    print('Please type it a valid note.')
    exit()

med = (nt1 + nt2) / 2

if med < 5.0:
    print('You went \033[1;31mdisapproved\033[m')
elif med > 5.0 and med < 6.9:
    print('You go to the \033[1;33mrecovery\033[m')
else:
    print('you went \033[1;32mapproved\033[m')