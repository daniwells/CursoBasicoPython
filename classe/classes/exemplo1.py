#EXEMPLO -> criando uma classe para clientes da Netflix

class Cliente:
    def __init__(self, name, email, Splan):
        self.name = name
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if Splan in self.lista_planos:
            self.Splan = Splan
        else:
            raise Exception("ERROR! Invalid plan")
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.Splan = novo_plano
        else:
            print("Invalid Plan")

    def ver_filme(self, filme, plano_filme):
        if self.Splan == plano_filme:
            print(f"ver filme {filme}")
        elif self.Splan == "premium":
            print(f"ver filme {filme}")
        elif self.Splan == "basic" and plano_filme == "premium":
            print("Upgrade to premium for watching this movie.")
        else:
            print("Invalid Plan.")

cliente1 = Cliente("Daniel", "daniellimafreita@gmail.com", "basic")
print(cliente1.Splan)
cliente1.ver_filme("Avatar 2", "premium")


cliente1.mudar_plano("premium")
print(cliente1.Splan)
cliente1.ver_filme("Avatar 2", "premium")