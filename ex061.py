n1 = int(input('type it the first number of arithmetic progression: '))
n2 = int(input('type it the reason of arithmetic progression: '))
count = 1


print('======== THE PROGRESSION ARITHMETIC ========')
print('{}'.format(n1), end='')
while count < 10:
    n1 = n1 + n2
    print(', {}'.format(n1), end='')
    count = count + 1
print(' END')