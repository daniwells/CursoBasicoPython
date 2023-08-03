n1 = int(input('type it the first number:'))
n2 = int(input('type it the second number:'))

if n1 > n2:
    print('\033[34mthe first number is bigger than the second number.\033[m')
elif n2 > n1:
    print('\033[34mthe second number is bugger than the first number.\033[m')
else:
    print('both the numbers are equals.')
