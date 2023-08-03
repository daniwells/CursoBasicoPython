n1 = int(input('type it a number:'))
double = n1 * 2
triple = n1 * 3
square_root = n1 ** (1/2)
print('the double is {}{}{}, the triple is {}{}{} and square root is {}{}{}'
      .format('\033[1;41m', double, '\033[m', '\033[1;42m', triple, '\033[m', '\033[1;43m', square_root, '\033[m'))
