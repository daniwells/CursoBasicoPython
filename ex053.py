import string

text = str(input('type it a text: '))

text = text.upper()

se = text.translate({ord(c): None for c in string.whitespace})

contr = se[-1::-1]

print('This text is read on the contrary {}'.format(contr))
if contr == se:
    print('this text is a palindrome.')
else:
    print('this text is not a palindrome.')

######################################################

#text = str(input('type it a text: '))

#text = text.upper()

#list = text.split()
#se = ''.join(list)

#contr = se[-1::-1]

#print('This text is read on the contrary {}'.format(contr))
#if contr == se:
    #print('this text is a palindrome.')
#else:
    #print('this text is not a palindrome.')




