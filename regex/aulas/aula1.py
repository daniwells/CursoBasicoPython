import re

#CARACTERES
#txt = 'ar\nra'
#txt = 'arara'
##########################################

"""standard = re.compile('ar.ra') #o ponto significa que pode ser qualquer caractere.
check = standard.findall(txt)
print(check)"""

##########################################

"""standard = re.compile(r'^a') #só retorna o primeiro caractere da primeira palavra, se não, não retorna nada.
standard2 = re.compile(r'[^a]') #retorna todos os caracteres, menos o selecionado.
check = standard.findall(txt)
check2 = standard2.findall(txt)
print(check)
print(check2)"""

##########################################

#txt2 = 'arara1992'
"""st = re.compile(r'\d') #Retorna todos os números
st2 = re.compile(r'\D') #Retorna todos MENOS os núneros
check = st.findall(txt2)
check2 = st2.findall(txt2)
print(check)
print(check2)"""

##########################################
#txt3 = """

#arara 1992

#"""
"""
st = re.compile(r'\s') #retorna todos os caracteres vazios, como quebras de linha e espaços.
st2 = re.compile(r'\S') #retorna todos os caracteres que NÃO são vazios.
check = st.findall(txt3)
check2 = st2.findall(txt3)
print(check)
print(check2)"""

##########################################

#txt4 = """

#_ara@ra 1992_

#"""

"""st = re.compile(r'\w') #retorna todos os alfanuméricos
st2 = re.compile(r'\W') #retorna todos menos os alfanuméricos
check = st.findall(txt4)
check2 = st2.findall(txt4)

print(check)
print(check2)"""

##########################################
#MÉTODOS

"""txt = 'arara'
st = re.compile(r'a')
check_findall = st.findall(txt) #método que retorna todos os caracteres iguais ao selecionado
check_match = st.match(txt) #métodos que retorna somente o primeiro caractere, se ele for igual ao selecionado
check_search = st.search(txt) #método que retorna uma vez o caractere selecionado
check_finditer = st.finditer(txt) #método que retorna todos os caracteres iguais aos selecionados + suas posições
print(check_findall)
print(check_match)
print(check_search)
print(check_finditer)

correspondence = check_finditer

for corr in correspondence:
    print(corr)"""

##########################################
#ESTUTURAS
    #Character set

txt="""
Arara 1992
"""

#st = re.compile(r'[a-zA-Z0-9@\n ]') #ESTE CONJUTO RETORNA TODOS OS CARACTERES SELECIONADOS
#correspondence = [corr for corr in st.finditer(txt)]
#print(correspondence)

#st = re.compile(r'[a-zA-Z] [0-9]') #UM COMPILE É APENAS UMA CONSULTA, OU SEJA, ESTE COMANDO NÃO RETORNARÁ TODOS OS
#CARACTERES E NÚMEROS, RETORNARÁ UM VALOR QUALQUER QUE TENHA um caractere, um espaço e um número -> NESTA EXATA SEQUÊNCIA

#correspondence = [corr for corr in st.finditer(txt)]
#print(correspondence)

#txt2="""
#Arara1992
#"""

"""
st = re.compile(r'[a-zA-Z]+ [0-9]+') #O "+" PERMITE QUE UM CONJUNTO RETORNE MAIS DE UM CARACTERE
correspondence = [corr for corr in st.finditer(txt2)]
print(correspondence)

st2 = re.compile(r'[a-zA-Z]+[0-9]+')
correspondence2 = [corr for corr in st2.finditer(txt2)]
print(correspondence2)"""

##########################################
    #QUANTIFICADORES

        # * -> O "*" irá verificar todos os caracteres, se o padrão aparecer ele o retorna, se não, retorna vazio

#txt = """
#Arara
#"""
"""st = re.compile(r'[ra]*') 
correspondence = [corr for corr in st.finditer(txt)]
print(correspondence)"""


        # + -> retorna todo o padrão quando está em sequência. ele só retorna quando o parão aparece.

#txt = """
#Arara
#"""
"""
st = re.compile(r'[ra]+') #retorna todo o padrão quando está em sequência. ele só retorna quando o parão aparece.
correspondence = [corr for corr in st.finditer(txt)]
print(correspondence)
"""

        # ? -> Retorna se for um "caractere" ou outro pelo menos uma vez, se não, retorna vazio.

#txt = """
#Arara
#"""
"""
st = re.compile(r'[ra]?') 
correspondence = [corr for corr in st.finditer(txt)]
print(correspondence)"""

        # {3} -> Retorna conforme o número de caracteres que delimitar

#txt = """
#Arara
#"""
"""
st = re.compile(r'[ra]{3}')
st2 = re.compile(r'[ra]{2}')
st3 = re.compile(r'[ra]{4}')
st4 = re.compile(r'[ra]{1}')
correspondence = [corr for corr in st4.finditer(txt)]
print(correspondence)
"""

        # {2,4} -> Retorna conforme uma quantidade mínima e máxima de caracteres.

#txt = """
#Arara
#"""
"""
st = re.compile(r'[ra]{2,4}')
correspondence = [corr for corr in st.finditer(txt)]
print(correspondence)"""

##########################################
    # GROUP
#txt = """
#Arara 1992
#arara 1993
#"""

"""
st = re.compile(r'(A|a)?[a-z]{4} [0-9]+')
correspondence = [corr for corr in st.finditer(txt)]
correspondence2 = [corr.group(0) for corr in st.finditer(txt)]
correspondence3 = [corr.group(1) for corr in st.finditer(txt)]
print(correspondence)
print(correspondence2)
print(correspondence3)"""

##########################################
    # EXEPLO 1:

#txt1 = """
##https://google.com/
#https://www.gov.br/
#https://www.kaiamba.com.br/
#http://www.faetec.rj.gov.br/
#"""
"""
#st = re.compile(r'https?://(www\.)?[a-zA-Z0-9]+\.(rj\.)?(com\.?|gov\.)?(br)?/')
st = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+\.)+([a-z]+)/')
correspondence = [corr for corr in st.finditer(txt1)]
correspondence2 = [corr.group(0) for corr in st.finditer(txt1)]
correspondence3 = [corr.group(1) for corr in st.finditer(txt1)]
correspondence4 = [corr.group(2) for corr in st.finditer(txt1)]
correspondence5 = [corr.group(3) for corr in st.finditer(txt1)]
print(correspondence)
print(correspondence2)
print(correspondence3)
print(correspondence4)
print(correspondence5)"""

##########################################

    # EXEMPLO 2:

emails = """
daniel@dominio.com
daniel.candiotto@dominio.com.br
DANIEL@dominio.br
DANIEL.CANDIOTTO@gov.br
danielcandiotto1@dominio1.co
daniel_candiotto_1@dominio-dominio.net
"""
st = re.compile(r'[a-zA-Z0-9]+((\.[a-zA-Z0-9]+|_[a-zA-Z0-9]+)+)?@([a-zA-Z0-9-_]+\.)+[a-zA-Z0-9-_]+')
correspondence = [corr for corr in st.finditer(emails)]
print(correspondence)




