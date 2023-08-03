name = input("Type it the product's name: ")
price = float(input("type it the product's price: "))

cprice = price
cthousant = 0
cheap = price
nc = [name]

print("""Do you want continue?

[1] = YES
[0] = NO

""")

leave = int(input(':'))

if price >= 1000:
    cthousant += 1

while leave > 1 or leave < 0:
    leave = int(input('(please, type it 1 or 0):'))

if price < cheap:
    cheap = price
    nc.append(name)

if leave == 0:
    print(f'The total value this purchase is {cprice}')
    print(f'The number of products more expensive than 1000R$ is {cthousant}')
    print(f'The cheapest product is: {nc[-1]}')
    exit()

while True:
    name = input("Type it the product's name: ")
    price = float(input("type it the product's price: "))
    cprice += cprice + price

    if price < cheap:
        cheap = price
        nc.append(name)

    if price >= 1000:
        cthousant += 1

    print("""Do you want continue?

    [1] = YES
    [0] = NO

    """)

    leave = int(input(':'))

    while leave > 1 or leave < 0:
        leave = int(input('(please, type it 1 or 0):'))

    if leave == 0:
        break

print(f'The total value this purchase is {cprice}')
print(f'The number of products more expensive than 1000R$ is {cthousant}')
print(f'The cheapest product is the {nc[-1]}')


