hv = float(input('type it the value of house:'))
s = float(input('type it your monthly salary:'))
y = int(input('type it the quantity of years that you ar going pay:'))

presta = (hv / y)
prest = presta / 12
t = s * 0.30
ta = t * 12

print('The value of provision is: {}'.format(presta))
print('tHE value of annual salary')

if prest <= t:
    print('You can pay the provision!')
else:
    print('You can not pay the provision!')