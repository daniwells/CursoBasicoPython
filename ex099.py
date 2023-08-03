from time import sleep
def write(txt):
    print('-='* 30)
    print(txt)


def mai(list):
    write('analyzing values...')
    sleep(1)
    if len(list) == 0:
        list.append(0)
        print(f'The values passed are 0, being them:', end=' ')
    else:
        print(f'The values passed are {len(list)}, being them:', end=' ')
    m = max(list)
    for v in list:
        print(f'{v}', end=' ')
    print(f'\nThe greatest value is {m}')


values = [1, 3, 8, 4, 2, 5]
mai(values)
valu = [10, 5, 2]
mai(valu)
val = [45, 77]
mai(val)
va = [7]
mai(va)
vl =  []
mai(vl)
