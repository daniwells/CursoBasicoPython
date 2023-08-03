def write(txt):
    print('-' * (len(txt) + 5))
    print(f'{txt:^{len(txt) + 5}}')
    print('-' * (len(txt) + 5))


text = input('Type it a text: ')
write(text)