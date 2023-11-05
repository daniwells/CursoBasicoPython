# Programação Imperativa

email = "daniel@gmail.com"

p = email.find('@')

serv = email[p:]

print(serv)

######################################################

# Programação orientada a objetos

class Email:
    def __init__(self):
        self.name = 'Daniel'
        self.email = "daniel@gmail.com"

    def pegar_servidor(self):
        p = self.email.find('@')
        serv = self.email[p:]

        print(serv)

email = Email()

email.pegar_servidor()