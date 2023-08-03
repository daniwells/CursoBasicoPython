c1 = float(input('type it the first lenght:'))
c2 = float(input('type it the second lenght:'))
c3 = float(input('type it the third lenght:'))

if abs(c2-c3) < c1 < c2 + c3:
    print('It is possible create a triangle.')
else:
    print('It is can not create a triangle.')