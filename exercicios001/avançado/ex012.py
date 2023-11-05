list = [21, 5, 34, 8, 16, 7, 3]

so = 0
sp = 0

for e in list:
    if e % 2 == 0:
        sp = sp + e
    else:
        so = so + e

print(so)
print(sp)
