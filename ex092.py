from datetime import date
name = input('Name: ')
y = int(input('Year of Birth: '))
ctps = int(input('Work Card (0 = not have): '))
today = date.today().year

age = today - y

dic = {
    'name':name,
    'age':age,
    'ctps':ctps,
}

if ctps != 0:
    h = int(input('Year of hiring: '))
    s = float(input('salary: '))
    ya = today - h
    ya2 = 35 - ya
    retirement = age + ya2
    dic['hiring'] = h
    dic['salary'] = s
    dic['retirement'] = retirement

for k, v in dic.items():
    print(f'{k} has the value {v}')