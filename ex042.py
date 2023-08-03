l1 = float(input('type it the first lenght:'))
l2 = float(input('type it the second lenght:'))
l3 = float(input('type it the third lenght:'))

if abs(l2-l3) < l1 < l2 + l3:
    if l1 == l2 == l3:
        print('This triangle is equilateral')
    #elif l1 == l2 and l2 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l3 != l1:
        #print('This triangle is isosceles')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('This triangle is escalene')
    else:
        print('This triangle is isosceles')
else:
    print('This sides cant to forma a triangle')
    exit()
