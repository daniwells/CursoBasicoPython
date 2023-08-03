n1 = int(input('type it the first number:'))
n2 = int(input('type it the second number:'))
n3 = int(input('type it the third number:'))

#list = [n1, n2, n3]

#print('The smaller number is: {}'.format(min(list)))
#print('The bigger number is: {}'.format(max(list)))

####################################################

#if n1 < n2 and n1 < n3:
    #print('The smaller number is: {}'.format(n1))
#if n2 < n1 and n2 < n3:
    #print('the smaller number is: {}'.format(n2))
#if n3 < n1 and n3 < n2:
    #print('the smaller number is: {}'.format(n3))

#if n1 > n2 and n1 > n3:
    #print('the bigger number is: {}'.format(n1))
#if n2 > n1 and n2 > n3:
    #print('the bigger number is: {}'.format(n2))
#if n3 > n2 and n3 > n1:
    #print('the bigger number is: {}'.format(n3))

####################################################

#if n1 > n2 and n1 > n3:
    #print('the bigger number is: {}'.format(n1))
#elif n2 > n1 and n2 > n3:
    #print('the bigger number is: {}'.format(n2))
#else:
    #print('the bigger number is: {}'.format(n3))

####################################################

smaller = n1

if n2 < n1 and n2 < n3:
    smaller = n2
if n3 < n1 and n3 < n2:
    smaller = n3
print('the smaller number is: {}'.format(smaller))
