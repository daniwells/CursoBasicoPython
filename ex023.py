num = input('type it a number of four digits:')

digit = num[:4]

print(digit)

print("""
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""".format(digit[3], digit[2], digit[1], digit[0]))
