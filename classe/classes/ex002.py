class Quad:

    def __init__(self, size_side):
        self.size_side = size_side

    def change_side(self, new_side):
        t = type(new_side) is int
        if t == False:
            t = type(new_side) is float

        if t == True:
            self.size_side = new_side
        else:
            print("ERROR! This don't a new valid value.")
            exit()

    def return_side(self):
        print(f"The side value is {self.size_side}")

    def cal_area(self):
        area = self.size_side * 2

        return area


while True:
    try:
        num = float(input('Enter the height of square: '))
    except:
        print('ERROR! Enter a valid number.')
    else:
        break

square = Quad(num)
square.return_side()

square.change_side(5.5)
square.return_side()

print(square.cal_area())
