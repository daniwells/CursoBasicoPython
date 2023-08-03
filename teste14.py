"""def line():
    print('-' * 30)


line()
print('Hello World')
line()
line()
print('Hi city')
line()
line()
print('OPAAAAAAAAAA')
line()
"""
############################################################
"""
def line(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)

line('Hello World')
"""
############################################################
"""
def soma(a, b):
    print(f'a = {a} and b = {b}')
    c = a + b
    print(c)


soma(4, 3)
soma(2, 6)
soma(b=7, a=5)
"""
############################################################
"""
def cont(*num):
    for v in num:
        print(f'{v} ', end='')
    print('END!')
    tan = len(num)
    print(f'The amount elements are {tan}.')


cont(1, 2, 3)
cont(5, 4, 5, 6, 10)
cont(3)
"""
############################################################

def db(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


list = [1, 2, 3, 5, 6]
print(list)
db(list)
print(list)
