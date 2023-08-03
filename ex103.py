def token(name='<unknown>', goals='0'):
    print(f'The player {name} did {goals} goals on the championship')



n = input('Type it the name of player: ')
g = input('Type it the amount of goals of player: ')

if n == '' and g == '':
    token()
elif n == '':
    token(goals=g)
elif g == '':
    token(name=n)
else:
    token(name=n, goals=g)


