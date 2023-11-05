from pacote import numbers

num = float(input('type it the price of product: '))

print(f'The haf of the number {num} is {numbers.half(num)}')
print(f'The double of the number {num} is {numbers.double(num)}')
print(f'increasing 10% in the number {num}, it becomes {numbers.increasing(num)}')
print(f'decreasing 13% in the number {num}, it becomes {numbers.decreasing(num)}')