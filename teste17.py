#TRATAMENTO DE ERRO
"""
print(x) #É uma exceção.
n = int(input('Num')) #Pode ser uma exceção, caso os usuários digitarem por exemplo
r = a/b #e se b=0(isso não pode acontecer na divisão)? Será uma exceção
r=2/'2' #"'2'" não é um numero! É uma exceção
lst=[3,6,4] print(lst[3]) #Não existe indice 3 nesta lista. É uma exceção
import uteis #e se uteis não existir? É uma exceção"""

###############################################################
"""
try:
    a = int(input('Type it a number: '))
    b = int(input('Type it a number: '))
    c = a / b
except:
    print('unfortunately we had a problem')
else:
    print(f'Resultado: {c}')
"""
###############################################################

"""
try:
    a = int(input('Type it a number: '))
    b = int(input('Type it a number: '))
    c = a / b
except Exception as error:
    print(f'The problem is <{error}>')
else:
    print(f'Resultado: {c}')
"""

###############################################################

try:
    a = int(input('Type it a number: '))
    b = int(input('Type it a number: '))
    c = a / b
#except Exception as error:
    #print(f'ERROR! <{error}>')
except (ValueError, TypeError):
    print('The type values are incorrect.')
except ZeroDivisionError:
    print(f"ERROR! You can't to divide a number for zero.")
except KeyboardInterrupt:
    print("The user don't informed the data.")
else:
    print(f'Resultado: {c}')
