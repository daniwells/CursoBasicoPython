list = [54, 10, 29, 87, 7, 64]

mai = 0
men = 0

for e in list:
    if mai == 0:
        mai = e
    elif e > mai:
        mai = e

    if men == 0:
        men = e
    elif e < men:
        men = e

print(men)
print(mai)