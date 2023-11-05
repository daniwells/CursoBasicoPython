import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 8888))

terminado = False
print('Digite tt para terminar o chat')

while not terminado:
    cliente.send(input('mensagem: ').encode('utf8'))
    msg = cliente.recv(1024).decode('utf8')
    if msg == 'tt':
        terminado = True
    else:
        print(msg)
cliente.close()