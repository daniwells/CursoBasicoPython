from time import sleep


def write(txt):
    print('-' * (len(txt) + 10))
    print(f'{txt:^{len(txt) + 10}}')
    print('-' * (len(txt) + 10))


write('Count of 1 to 10!')
for c in range(1, 11):
    print(c, end=' ')
    sleep(0.5)
print('END!')

print('\n')

write('Count of 10 to 0!')
for c in range(10, -1, -1):
    print(c, end=' ')
    sleep(0.5)
print('END!')

print('\n')


def cont(st, end, pa):
    write(f'Count of {st} to {end} of {pa} by {pa}:')
    for c in range(st, end, pa):
        print(c, end=' ')
        sleep(0.5)
    print('END!')

write('Now is your turn! Create a person counter: ')

start = int(input('START: '))
end = int(input('END: '))
step = int(input('STEP: '))

if start > end:
    step = -step

if step == 0:
    if start > end:
        step = -1
    else:
        step = 1


cont(start, end, step)
