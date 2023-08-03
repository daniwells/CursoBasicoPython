phrase = input('Type it a phrase:')

print(phrase.upper().replace('Á', 'A').replace('À', 'A').replace('Ã', 'A').replace('Â', 'A').replace('Ä',
     'A').replace('Å	', 'A').count('A'))
print(phrase.upper().replace('Á', 'A').replace('À', 'A').replace('Ã', 'A').replace('Â', 'A').replace('Ä',
     'A').replace('Å', 'A').find('A'))
print(phrase.upper().replace('Á', 'A').replace('À', 'A').replace('Ã', 'A').replace('Â', 'A').replace('Ä',
     'A').replace('Å', 'A').rfind('A'))


