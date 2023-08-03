student = {}

name = input('Name: ')
med = float(input('Average: '))

if med > 6.9:
    sit = 'approved'
elif 5 <= med < 7:
    sit = 'recovery'
else:
    sit = 'disapproved'

student['name'] = name
student['media'] = med
student['situation'] = sit

print('-=' * 30)

for k, v in student.items():
    print(f'{k} = {v}')

print()
print(f'The situation of student {student["name"]} is {student["situation"]}')