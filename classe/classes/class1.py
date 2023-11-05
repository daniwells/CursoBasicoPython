class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o Canal")
        elif botao == "-":
            print("Diminuir o Canal")

controle_remoto = ControleRemoto("preto", "12cm", "2cm", "3cm")
print(controle_remoto.altura)

controle_remoto.passar_canal("+")

controle_remoto2 = ControleRemoto("cinza", "12cm", "2cm", "3cm")
print(controle_remoto2.cor)