def factorialRec(num):
    if num == 0:
        return 0
    elif num > 1:
        num = num * factorialRec(num-1)
    return num

print(factorialRec(5))

def factorialFor(num):

    for c in range(num, 1, -1):
        num *= (c-1)

    return num

print(factorialFor(5))