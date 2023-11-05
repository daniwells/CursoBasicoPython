class rect:
    def __init__(self, c, h, per=0, ar=0):
        self.c = c
        self.h = h
        self.per = per
        self.ar = ar

    def change(self, new_c=0, new_h=0):
        if new_c != 0:
            self.c = new_c

        if new_h != 0:
            self.h = new_h

    def return_values(self):
        print(f'The length is {self.c} and the height is {self.h}')

    def per_ar(self):
        self.per = (self.c * 2) + (self.h * 2)
        self.ar = self.c * self.h

rectangle = rect(4.3, 5)
rectangle.return_values()

rectangle.change(6.4, 9)
rectangle.return_values()

rectangle.per_ar()
print(rectangle.per, rectangle.ar)

area = float(input("Enter the area of local: "))
length = float(input("Enter the length of local: "))

answer = rect(area, length)

answer.per_ar()

print(f"The amount of floor that you need are {answer.ar}m and the amount of baseboard is {answer.per}m")
