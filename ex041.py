from datetime import date

d = int(input('type it your year of birth:'))

age = date.today().year - d

print('The athlete has {} years'.format(age))

if age <= 9:
    print('Your category is \033[35mMIRIM.\033[m')
elif 14 >= age > 9:
    print('Your category is \033[36mINFANTIL\033[m')
elif 19 >= age > 14:
    print('Your category is \033[34mJUNIOR\033[m')
elif 25 >= age > 19:
    print('Your category is \033[37mSÊNIOR\033[m')
elif age > 25:
    print('Your category is \033[31mMASTER\033[m')