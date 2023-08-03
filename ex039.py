from datetime import date

y = int(input('type it the year of birth:'))

age = date.today().year - y

if age < 18:
    af = 18 - age
    print('You will still enlist!')
    print('\033[32m{} years left\033[m'.format(af))
elif age == 18:
    print('\033[33mit is time from you enlist!\033[m')
elif age > 18:
    af = age - 18
    print('the time of enlistment already happened!')
    print('\033[31m{} years passed!\033[31m'.format(af))





