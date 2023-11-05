import mysql.connector

#DADOS PARA A REALIZAÇÃO DA CONEXÃO
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdyoutube',
)

cursor = conexao.cursor()

#CRUD

#CREATE
"""nome_produto = "picanha"
valor = 99
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {10})'
cursor.execute(comando)
conexao.commit() #quando edita o banco de dados você precisa dar um commit"""

#READ
"""
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #usado sempre que você for ler o banco de dados
for i in resultado:
    print(i)"""

#UPDATE
"""comando = f'UPDATE vendas SET nome_produto = "Nescau", valor = 4 WHERE id = 1'
cursor.execute(comando)
conexao.commit() #quando edita o banco de dados você precisa dar um commit"""

#DELETE
"""comando = f'DELETE FROM vendas WHERE id = 2'
cursor.execute(comando)
conexao.commit() #quando edita o banco de dados você precisa dar um commit"""


#FINALIZAÇÃO DA CONEXÃO
cursor.close()
conexao.close()

