n = int(input('type it a integer number: '))

n2 = 0
c = 1
count = 1
max = n
min = n

while c == 1:
    n2 = int(input('type it a integer number: '))

    n = n + n2
    count = count + 1
    med = n / count
    if n2 > max:
        max = n2
    if n2 < min:
        min = n2

    print('The avarege this numbers is: \033[33m{}\033[m'.format(med), end='. ')
    print('The gratest number is: \033[33m{}\033[m'.format(max), end='. ')
    print('The smallest number is: \033[33m{}\033[m'.format(min), end='. ')

    print("""\nAre you want to continue?

        [1] = YES
        [0] == NO

        """)
    c = int(input('Your choice: '))
print('END')