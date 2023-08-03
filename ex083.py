exp = input('Type it an expression: ')

p = []

space = ''

for c in exp:
    space += c + ' '

for b in space:
    if b == '(' or b == ')' or b == '((' or b == '))':
        p.append(b)

q = len(p)

if q % 2 == 0:
    print('the number of parentheses is correct.')
else:
    print("the number of parentheses isen't correct.")

