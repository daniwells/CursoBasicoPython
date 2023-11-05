"""preco = 1000

def calcular_imposto(val):
    return val * 0.3

print(calcular_imposto(preco))

calcular_imposto2 = lambda preco: preco * 0.3

print(calcular_imposto2(preco))"""

precos = [100, 500, 10, 25]

impostos = list(map(lambda x: x * 0.3,precos))
print(impostos)