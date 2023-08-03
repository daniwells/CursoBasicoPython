from datetime import date

def vote(age):
    a = date.today().year - age
    return a

birth = int(input('Type it your year of birth: '))

if 65 > vote(birth) >= 18:
    print(f'With {vote(birth)}, the vote is mandatory.')
elif 16 <= vote(birth) < 18 or vote(birth) >= 65:
    print(f'With {vote(birth)}, the vote is optional.')
else:
    print(f"With {vote(birth)}, don't vote.")