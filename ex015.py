n1 = float(input('type it the amount of days you rented the car:'))
n2 = float(input('type it the amount of kilometer traveled:'))

result1 = n1 * 60
result2 = n2 * 0.15
resultf = result1 + result2

print('the price to pay is: {}'.format(resultf))
