"""
with open('email.txt', 'r') as arquivo:
    email = arquivo.read() #Usado para ler arquivos simples, com apenas uma linha
print(email) #Todo o texto será uma string
"""
############################################################################################
"""
with open('mensagem.txt', 'r', encoding="UTF-8") as mensagem:
    msg = mensagem.readlines() #usado para ler textos grandes

print(msg) #Cada linha do texto será um item de uma lista.
for l in msg:
    if 'faturamento' in l:
        print(l)
"""
############################################################################################
"""
#Substituindo a informação de um arquivo:

with open('senha.txt', 'w') as se:
    se.write('4321')

with open('senha.txt', 'r') as arq:
    senha = arq.read()

print(senha)

#Criando um arquivo novo:

with open('nova_senha', 'w') as ns:
    ns.write('234545363456')
"""
############################################################################################

#Adicionando um texto em um arquivo de texto:

with open('email.txt', 'a') as arq:
    arq.write('\njuliano33@gmail.com') #\n = "ENTER"