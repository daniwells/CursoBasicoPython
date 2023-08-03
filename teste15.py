#help(print)
#print(input.__doc__)

#################################################################################

'''
def cont(s, e, p):
    """
    :param s: Start of count
    :param e: End of count
    :param p: Step of count
    :return: The values of s to e counting of p by p
    """
    for c in range(s, e + 1, p):
        print(c, end=' ')
    print(end='')


cont(0, 20, 2)

help(cont)

'''

#################################################################################

#igualar os parâmetros a 0 para criar parâmetros opcionais.

"""
def soma(a=0, b=0, c=0):
    x = a + b + c
    print(x)


soma()
soma(b=3)
soma(2, 4)
"""

#################################################################################
"""
def teste():
    y = 4
    print(f'In the function  teste, y is equal to {y}')
    print(f'In the function teste, x is equal to {x}')

x = 9
print(f'In the principal program, x is equal to {x}')
print(f'In the principal program, y is equal to {y}')

# A variável y é local, portanto só existe dentro da função "teste"
# e esse programa retornará um erro
"""

"""
def fun():
    n1 = 4
    print(f'n1 inside of function is equal to {n1}')


n1 = 2
print(f'n1 global is equal to {n1}')
"""

#TRATANDO UMA VARIAVEL GLOBAL COMO GLOBAL MESMO DENTRO DA FUNÇÃO
"""
def fun():
    global n1 #define n1 como global dentro da função
    n1 = 4
    print(f'n1 inside of function is equal to {n1}')


n1 = 2
print(f'n1 global is equal to {n1}')
"""
#################################################################################
"""
def soma(a=0, b=0, c=0):
    x = a + b + c
    return x


r1 = soma()
r2 = soma(b=3)
r3 = soma(2, 4)

print(f'The results were {r1} and {r2} and {r3}')

#o comando retorno adiciona toda a função em uma variável
"""

#################################################################################
"""
def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

f1 = fatorial(2)
f2 = fatorial(10)
f3 = fatorial()
print(f'{f1} {f2} {f3}')
#num = int(input('Type it a number: '))
#print(f'The factorial of {num} is {fatorial(num)}')
"""

def pairOrOdd(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('type it a number: '))
if pairOrOdd(num):
    print('Is pair!')
else:
    print("don't is pair!")
