from pacote import numbers

num = float(input('type it the price of product: '))

print(f'The haf of the number {numbers.coin(num)} is {(numbers.half(num, f=True))}')
print(f'The double of the number {numbers.coin(num)} is {(numbers.double(num, f=True))}')
print(f'increasing 10% in the number {numbers.coin(num)}, it becomes {(numbers.increasing(num, f=True))}')
print(f'decreasing 13% in the number {numbers.coin(num)}, it becomes {(numbers.decreasing(num, f=True))}')