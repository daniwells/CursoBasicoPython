km = float(input('type it the distance of trip:'))

if km <= 200:
    print('The price of trip is: {:.2f}'.format(km * 0.50))
else:
    print('The price of tripe is: {:.2f}'.format(km * 0.45))
