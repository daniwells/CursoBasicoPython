#EXEMPLO 1
"""list_user = str(input('Enter numbers:'))
numbers = list_user.split(",")

list = [float(e) for e in numbers]
list2 = [float(e)**2 + 4 for e in numbers]

cont = 0
for e in numbers:
    numbers[cont] = float(e)
    cont += 1"""

#########################################
"""def rep(key, message, replacement):
    message = list(message)
    message[key - 1] = replacement
    message = ''.join(message)
    return message
    #return message.replace(message[key - 1], replacement)
#######
number = 2
txt = 'cavalo'

print(rep(2, 'cavalo', 'e'))"""

#########################################
#EXEMPLO 2
"""
key = 2
message = 'abacaxi'

n = 128

list = [chr((ord(letter) + key)%n) for letter in message]

encrypted = "".join(list)
print(encrypted)
#######
for letter in message:
    new_letter = chr((ord(letter) + key)%128)
    encrypted = encrypted + new_letter"""

#########################################
#EXEMPLO 3

"""list_price = [500,1500,2000,100,25]

new_list_price = [p * 2 for p in list_price]
print(new_list_price)"""
#########################################
#EXEMPLO 4
list_price = [500,1500,2000,100,25]

"""list_price2 = []
for e in list_price:
    if e >= 1000:
        tax = e * 0.5
        e = e + tax
    list_price2.append(e)

print(list_price2)"""

list_price2 = [e + (e * 0.5) for e in list_price if e >= 1000]
print(list_price2)
