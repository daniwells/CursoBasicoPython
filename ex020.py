import random

na1 = input('type it the first name:')
na2 = input('type it the second name:')
na3 = input('type it the third name:')
na4 = input('type it the fourth name:')

list = [na1, na2, na3, na4]

f = random.shuffle(list)

print(list)

print(' The first to submit is {}, the second is {}, the third is {}, the fourth is {}'.format(list[0], list[1],
list[2], list[3]))



