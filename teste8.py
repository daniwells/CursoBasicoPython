#for c in range(1,11):
    #print(c)
#print('End')

#c = 1
#while c < 11:
    #print(c)
    #c = c + 1
#print('End')

#########################

#valor = 1
#while valor != 0:
    #valor = int(input('type it the value:'))
#print('End')

##########################

#r = 'S'

#while r == 'S':
    #int(input('type it a value: '))
    #r = input('type it if you want continue(S, N): ').upper()

##########################

n = 1
pair = 0
odd = 0

while n != 0:
    n = int(input('Type it a number: '))
    if n != 0:
        if n % 2 == 0:
            pair = pair + 1
        else:
            odd = odd + 1

print('Are {} pairs'.format(odd))
print('Are {} odd'.format(pair))

