def error(n):
    while True:
        try:
            number = float(input(n))
        except:
            print('Enter a valid integer number!')
        else:
            break
    return number

list = []

for c in range(0, 4):
    nt = error(f'Enter the grade: ')
    list.append(nt)

med = sum(list) / len(list)

if med >= 7:
    print('Do you were approved')
else:
    nf = error('Enter the final grade: ')
    list.append(nf)
    med = sum(list) / len(list)
if med >= 5:
    print('Do you were approved')
else:
    print('Do you were disapproved')