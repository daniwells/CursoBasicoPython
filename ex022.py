name = input('type it your complete name:')

name = name.strip()

print('The name in upper: {}'.format(name.upper()))
print('The name in lower: {}'.format(name.lower()))

kspace = int(name.count(' '))
total = int(len(name))

print('The number letter of name: {}'.format(total - kspace))

list = name.split()

print('The number letter of first name: {}'.format(len(list[0])))





