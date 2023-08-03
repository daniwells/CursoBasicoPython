import random

na1 = input('type it the first name:')
na2 = input('type it the second name:')
na3 = input('type it the third name')
na4 = input('type it the fourth name')

p = [na1, na2, na3, na4]

ne = random.choice(p)

print(ne)
