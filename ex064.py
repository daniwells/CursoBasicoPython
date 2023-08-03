num2 = int(input('type it a integer number: '))

num = 0
count = 0

while num != 999:
    num = int(input('type it a integer number: '))
    num2 = num2 + num
    count = count + 1
print('The sum of digits is: {} '.format(num2 - 999))
print('You typed {} digits.'.format(count))
