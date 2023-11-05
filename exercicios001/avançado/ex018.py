def monthForExtenxive(month):
    if month == '01':
        month = 'January'
    elif month == '02':
        month = 'February'
    elif month == '03':
        month = 'March'
    elif month == '04':
        month = 'April'
    elif month == '05':
        month = 'May'
    elif month == '06':
        month = 'June'
    elif month == '07':
        month = 'July'
    elif month == '08':
        month = 'August'
    elif month == '09':
        month = 'September'
    elif month == '10':
        month = 'October'
    elif month == '11':
        month = 'November'
    elif month == '12':
        month = 'December'

    return month

def confirm(p):
    while True:
        d = input(p)

        if len(d) == 2:
            d = int(d)
            if 32 > d > 0:
                break
            else:
                print('Error! Type it a valid number.')
        else:
            print('Error! Type it in the correct format: (dd/mm/aaaa).')

    return d


print('Enter a date this dd/mm/aaaa format!')



day = confirm('Enter a day: ')

if day < 10:
    day = str(f'0{day}')

month = confirm('Enter a month: ')


while True:
    if month > 12 or month < 1:
        print('Error! Type it a valid month.')
        month = confirm('Enter a month: ')
    else:
        if month < 10:
            month = str(f'0{month}')
        else:
            month = str(month)
        break

month = monthForExtenxive(month)

while True:
    try:
        year = int(input('Enter a year: '))
    except:
        print('Enter a correct value!')
    else:
        year = str(year)
        if len(year) == 4:
            break
        else:
            print('Error! Type it in the correct format: dd/mm/aaaa.')




print(f'{day}/{month}/{year}')
