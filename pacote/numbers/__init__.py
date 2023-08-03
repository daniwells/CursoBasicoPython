def coin(n):
    c = f'R${n:.2f}'
    c2 = str(c)
    c3 = c2.replace('.', ',')
    return c3


def factorial(num, f=False):
    f = 1
    for c in range(1, num + 1):
        f = f * c
    return f


def half(n, f=False):
    h = n / 2
    if f == True:
        return coin(h)
    else:
        return h


def double(n, f=False):
    d = n * 2
    if f == True:
        return coin(d)
    else:
        return d



def increasing(n, f=False):
    i = n * 0.10
    i2 = n + i

    if f == True:
        return coin(i2)
    else:
        return i2


def decreasing(n, f=False):
    d = n * 0.13
    d2 = n - d

    if f == True:
        return coin(d2)
    else:
        return d2


def resume(n, i, d):
    incr = i / 100
    inc = n * incr
    inc2 = n + inc

    decre = d / 100
    dec = d * decre
    dec2 = d - dec

    print('-' * 50)
    print(f'{"RESUME OF VALUE":^50}')
    print('-' * 50)

    print(f'The half of price is:             {coin(half(n))}')
    print(f'The double of price is:           {coin(double(n))}')
    print(f'The price more {inc:.2f}% is:         {coin(inc2)}')
    print(f'The price minus {dec:.2f}% is:        {coin(dec2)}')
    print('-' * 50)

def readInt(ni):
    while True:
        try:
            num = int(input(ni))
        except KeyboardInterrupt:
            print("The user don't typed the value, then value is 0")
            num = 0
            print(f'The integer value typed was \033[32m{num}\033[m')
        except:
            print('\033[1;31mERROR! Type it a valid integer number.\033[m')
        else:
            print(f'The integer value typed was \033[32m{num}\033[m')
            break

def readFloat(nf):
    while True:
        try:
            num2 = float(input(nf))
        except KeyboardInterrupt:
            print()
            print("The user don't typed the value, then value is '0'")
            num2 = 0
            print(f'The real number typed was \033[32m{num2}\033[m')
            break
        except:
            print('\033[1;31mERROR! Type it a valid real number.\033[m')
        else:
            print(f'The real number typed was \033[32m{num2}\033[m')
            break




