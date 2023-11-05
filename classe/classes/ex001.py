class ball:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    def mostra_cor(self):
        print(self.cor)


ball1 = ball("red", "40cm", "rubber")
ball1.mostra_cor()

ball1.troca_cor("blue")
ball1.mostra_cor()