n1 = int(input('type it the first number of arithmetic progression: '))
n2 = int(input('type it the reason of arithmetic progression: '))
count = 10
mt = 1


print('======== THE PROGRESSION ARITHMETIC ========')
print('{}'.format(n1), end='')
while mt == 1:
    while count > 1:
        n1 = n1 + n2
        print(', {}'.format(n1), end='')
        count = count - 1
    mt = int(input("""\nYou want to add more terms?
    [1] YES
    [0] NO
    """))
    if mt == 1:
        amount = int(input('type it the amount of terms that you want: '))
        count = count + amount
    elif mt == 0:
        count = 1

print(' END')
