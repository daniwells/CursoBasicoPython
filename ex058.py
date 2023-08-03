import random

pc = random.randint(1, 10)

digit = int(input('type it a value between 1 to 10: '))

count = 1
if digit != pc:
    print('the value not is {}'.format(digit))
    while digit != pc:
        digit = int(input('type it a value between 1 to 10 again: '))
        count = count + 1
        if digit != pc:
            print('not is {}'.format(digit))
print('You are right, the value is {}. Were needed {} guesses.'.format(digit, count))
