s = float(input('type it you salary:'))

if s > 1250:
    au1 = s * 0.1
    print('Your new salary is: {:.2f}'.format(s + au1))
else:
    au1 = s * 0.15
    print('Your new salary is: {:.2f}'.format(s + au1))


