num = int(input('type it a whole number:'))
print("""You want that the number to be from which base?
    If it is binary, type it \033[4;31m1\033[m. 
    If it is octal, type it \033[4;31m2\033[m. 
    If it is hexadecimal, type it \033[4;31m3\033[m""")

b = input('Your choice: ')

if b == '1':
    num = bin(num)
    print(num[2:])
elif b == '2':
    num = oct(num)
    print(num[2:])
elif b == '3':
    num = hex(num)
    print(num)
else:
    print('please type it a number of 1 to 3!')

