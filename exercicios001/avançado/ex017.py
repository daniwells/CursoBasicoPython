vh = float(input('Enter your value for worked hours: '))
hm = int(input('Enter the amount of worked hours in the month: '))

sb = vh * hm

ir = 0

if sb <= 900:
    ir = 0
elif sb <= 1500:
    ir = sb * 0.05
elif sb <= 2500:
    ir = sb * 0.1
elif sb > 2500:
    ir = sb * 0.2

FGTS = sb * 0.11

INSS = sb * 0.1

td = INSS + ir

sl = sb - ir - INSS

print(f"""
{'Salário Bruto':<30}: R$ {sl}
{'IR':<30}: R$ {ir}
{'INSS':<30}: R$ {INSS}
{'FGTS':<30}: R$ {FGTS}
{'Total De Descontos':<30}: R$ {td}
{f'Salário liquido':<30}: R$ {sl}
""")