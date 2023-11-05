from pacote import numbers

num = float(input('type it the price of product: '))

print(f'The haf of the number {numbers.coin(num)} is {numbers.coin(numbers.half(num))}')
print(f'The double of the number {numbers.coin(num)} is {numbers.coin(numbers.double(num))}')
print(f'increasing 10% in the number {numbers.coin(num)}, it becomes {numbers.coin(numbers.increasing(num))}')
print(f'decreasing 13% in the number {numbers.coin(num)}, it becomes {numbers.coin(numbers.decreasing(num))}')