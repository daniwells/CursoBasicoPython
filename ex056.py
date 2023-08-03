med = 0
cad = []
old = []
id = 0
w = 0
m = 0
for c in range(1, 5):
    print('===== {}° people ====='.format(c))
    name = input('type it your name: ')


    age = int(input('type it age in years: '))
    med = med + age

    print("""type it your sex: 
    [1] masculine
    [2] feminine
    [3] other
    """)
    sex = int(input('Your choose: '))

    if sex == 1 or sex == 2 or sex == 3:
        if sex == 1:
            m = m + 1
            if age >= id:
                id = age
                old.append(name)
        elif sex == 2:
            if age < 20:
               w = w + 1
    else:
        print('type it a correct number!!!')
        exit()

if m > 0:
    print('The man older is {} with {} years'.format(old[-1], id))
print('The average of age is {}'.format(med / 4))
print('The number of women with age smaller than 20 is {}'.format(w))
