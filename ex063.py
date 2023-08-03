n1 = int(input('type it a number: '))
n2 = int(input('Type it the amount of terms: '))

print(n1)
print(n1)
n3 = n1 + n1
while n2 > 1:
    n1 = n1 + n3
    n3 = n1 + n3
    n2 = n2 - 1
    print(n1)
    print(n3)