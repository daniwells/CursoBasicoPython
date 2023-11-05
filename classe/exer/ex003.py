class Vendedor():
    def __init__(self, name):
        self.name = name
        self.vendas = 0
    def vendeu(self, vendas):
        self.vendas = vendas
    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.name, "Bateu a meta.")
        else:
            print(self.name, "Não bateu a meta.")

vend1 = Vendedor("Daniel")
vend1.vendeu(1200)
vend1.bateu_meta(1000)

vend2 = Vendedor("Marcos")
vend2.vendeu(500)
vend2.bateu_meta(1000)