def error(n):
    while True:
        try:
            num = float(input(n))
        except:
            print('Type it a valid number!')
        else:
            break
    return num

def exp(num1, num2):
    print("""
Do you want make expression?

        [0] - SUM
        [1] - REDUCTION
        [2] - MULTIPLICATION
        [3] - DIVISION
        [4] - EXPONENTIATION
                """)
    while True:
        try:
            ex = int(input('Your choice: '))
        except:
            print('Type it a valid option.')
        else:
            if 0 <= ex < 5:
                break
            print('Enter a valid option')



    result = 0

    if ex == 0:
        result = num1 + num2
    elif ex == 1:
        result = num1 - num2
    elif ex == 2:
        result = num1 * num2
    elif ex == 3:
        result = num1 / num2
    elif ex == 4:
        result = num1 ** num2

    return result


cont = 2
n1 = error('type it the 1º number: ')
n2 = error('type it the 2º number: ')

re = exp(n1, n2)
print()
print(f'The result is: {re}')
print()

while True:
    print('Do you want continue?(Y/N)')
    c = input('Your choice: ').upper()

    while c != 'Y' and c != 'N':
        c = input('Please, enter "Y" or "N": ').upper()

    if c == 'Y':
        cont += 1
        n3 = error(f'Enter the {cont}º number: ')
        re2 = exp(re, n3)
        print()
        print(f'The result is: {re2}')
        print()
        re = re2
    elif c == 'N':
        break