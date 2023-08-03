def readData(d):
    list = []
    num = input(d)
    list.append(num)

    if ',' in num:
        num = num.replace(',', '')
    if '.' in num:
        num = num.replace('.', '')

    while num.isnumeric() is False:
        num = input('Error! Type it a valid number: ')
        list.append(num)
        if ',' in num:
            num = num.replace(',', '')
        if '.' in num:
            num = num.replace('.', '')

    if ',' in list[-1]:
        list[-1] = list[-1].replace(',', '.')
    list[-1] = float(list[-1])
    return list[-1]



