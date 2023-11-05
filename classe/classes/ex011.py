class car:
    def __init__(self, km):
        self.km = km
        self.tank = 0

    def addGasoline(self, amountLiter):
        self.tank = amountLiter

    def showGasoline(self):
        print(f'Your tank is with {self.tank}L')

    def run(self, runKm):
        l = runKm // self.km

        if self.tank <= 0:
            self.tank = 0
            print("Your tank is empty, you can't running!")
        else:
            self.tank = self.tank - l

            if self.tank < 0:
                self.tank = 0
                print('Your tank is empty!')

car1 = car(40)

car1.addGasoline(55)

car1.run(700)

car1.showGasoline()
