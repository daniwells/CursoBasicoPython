text = input('type it your name:')
print('pleasure to meet you {:=^50}!'.format(text))

n1 = int(input('type it a value:'))
n2 = int(input('type it a other value:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
so = n1 % n2

print('The sum is {}! \n The multiplication is {}! \n The division is {}! \n The whole division is {}! \n The leftover is {}!'.format(s, m, d, di, so))
print('the final cont is: {}"'.format(s+m+d+di+so))




