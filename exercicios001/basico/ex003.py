def error(n):
    while True:
        try:
            number = int(input(n))
        except KeyboardInterrupt:
            print('No data has been entered.')
        except (TypeError, ValueError):
            print('Please, Type it a valida integer number.')
        except Exception as exc:
            print('ERROR! There was a unexpeted error.')
        else:
            break
    return number

n = error('Type it a number: ')

if n % 2 == 0:
    print('This number is pair')
else:
    print('This number is odd')