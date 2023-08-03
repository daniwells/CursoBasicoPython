from time import sleep

print('the fireworks will explosion in...')

sleep(0.5)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;31m{:=^40}\033[m'.format(' EXPLOSION '))
