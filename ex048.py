list = []
for c in range(3, 501, 3):
    if c % 2 == 1:
        #print(c, end=' ')
        list.append(c)
print('The sum of requested values is {}'.format(sum(list)))
print('Are {} values'.format(len(list)))


#list = []
#for c in range(3, 501, 3):
    ##if c % 2 == 1:
        #print(c, end=' ')
        #list.append(c)
        #print(list)
