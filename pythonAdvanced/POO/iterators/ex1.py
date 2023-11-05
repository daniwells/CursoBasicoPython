cars = ['HRV','polo','jetta','Cruze','Fusion']

itCars=iter(cars)

while True:
    try:
        print(next(itCars))
    except:
        break

