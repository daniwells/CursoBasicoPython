list = []

for c in range(0, 4):
    while True:
        try:
            n = float(input(f'Enter the {1}º note: '))
        except:
            print('Enter a valid integer number!')
        else:
            break
    list.append(n)

media = sum(list) / 4
max = max(list)
min = min(list)

print(media)
print(max)
print(min)