while True:
    n = int(input("""----------------------------------------
    type it a integer number: """))

    if n < 0:
        break

    print("""The multiplication table this number is: 
----------------------------------------""")

    for c in range(1, 11):
        print(f"""{n} X {c} = {n * c}""")


print('END')
