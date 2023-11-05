from datetime import date

day = date.today().day
month = date.today().month
year = date.today().year

if month < 10:
    zero = 0
else:
    zero = ''

if day < 10:
    zero2 = 0
else:
    zero2 = ''

print(f'Today date: {zero2}{day}/{zero}{month}/{year}')
print(f'Two days in the future{zero2}{day + 2}/{zero}{month}/{year}')
