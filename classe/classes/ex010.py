class BombaCombustivel:
    def __init__(self, fuelType, valueLiter, fuelAmount):
        self.fuelType = fuelType
        self.valueLiter = valueLiter
        self.fuelAmount = fuelAmount

    def supply_value(self, supplyValue):
        cont = 0
        liter = 0

        while True:
            cont = cont + self.valueLiter

            self.fuelAmount += 1
            liter += 1

            if cont >= supplyValue:
                print(f'Supply complete. It was stocked {liter}L of fuel.')
                break

            if self.fuelAmount >= 55:
                print('Your tank is full.')
                print(f'Left {supplyValue - cont} R$.')
                break

    def supply_liter(self, amountLiter):
        value = 0
        for c in range(0, amountLiter):
            self.fuelAmount += 1
            value += self.valueLiter

            if self.fuelAmount >= 55:
                print('Your tank is full.')
                break
        print(f'The price of supply is {value:.2f}R$.')

    def changeFuelValue(self, newValue):
        self.valueLiter = newValue

    def changeFuelType(self, newType):
        self.fuelType = newType

    def changeFuelAmount(self, newAmount):
        self.fuelAmount = newAmount


carro1 = BombaCombustivel('Etanol Comum', 5.30, 22)


print(carro1.fuelType)
print(carro1.valueLiter)
print(carro1.fuelAmount)

print()

carro1.supply_value(20.50)

carro1.supply_liter(20)

print()

carro1.changeFuelType('Gasolina Comum')
print(carro1.fuelType)

carro1.changeFuelValue(7.40)
print(carro1.valueLiter)

carro1.changeFuelAmount(9)
print(carro1.fuelAmount)

carro1.supply_value(20.50)

carro1.supply_liter(20)







