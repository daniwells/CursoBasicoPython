def error(num):
    while True:
        try:
            n = int(input(num))
        except:
            print('There was a error, enter a valid number!')
        else:
            if 11 > n >= 0:
                break
            print('Enter a valid number!!')
    return n
