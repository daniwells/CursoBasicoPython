speed = float(input('type it the speed of your car during this race:'))

tt = speed - 80

if speed > 80:
    print('You exceeded the limit of speed!')
    print('your traffic ticked is {:.2f}'.format(tt * 7))
else:
    print('keep it up.')
