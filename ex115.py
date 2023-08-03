from pacote import strings


def menu(option):
    while True:

        strings.tittle('Main menu')

        print("""
1 - See registered people.
2 - Register a new people
3 - Leave of the system.
        """)
        print('-' * 40)

        while True:
            try:
                c = int(input(option))
            except Exception as error:
                print(f'ERROR! <{error}>')
            else:
                if 4 > c > 0:
                    break
                else:
                    print('ERROR! Type it a correct number.')

        if c == 3:
            print('Good bye. Always come back!.')
            break
        elif c == 2:

            while True:
                try:
                    name = input('Type it a name to be registered: ')
                except Exception as e:
                    print(f'ERROR! <{e}>')
                else:
                    if name.isalpha() is True:
                        break
                    print('Please, type it a valid name.')
            while True:
                try:
                    age = int(input('Type it the age of people: '))
                except Exception as e:
                    print(f'ERROR! <{e}>')
                else:
                    break

            try:
                with open('register.txt', 'r') as i:
                    ip = i.readlines()
            except:
                with open('register.txt', 'w') as arq:
                    arq.write(f"\n{1}-{name:<30} {age} years")
            else:
                #if len(ip) == 0:
                    #ip2 = 1
                #else:
                ip2 = len(ip)
                with open('register.txt', 'a') as ad:
                    ad.write(f"\n{ip2}-{name:<30} {age} years")

        elif c == 1:
            strings.tittle('Registered People')
            with open('register.txt', 'r', encoding="UTF-8") as re:
                reg = re.readlines()
            for e in reg:
                print(e)



choice = menu('Your choice: ')
