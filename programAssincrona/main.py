import time
import asyncio


print("PROGRAMAÇÃO ASSÍNCRONA")
print("-"*30)
async def calculateTax(invoicing):
    print(invoicing * 0.1)
    #return invoicing * 0.1


async def calculate_bonus_workers(sales):
    for workers in sales:
        sale = sales[workers]
        print(workers, "bonus", sale * 0.05)
        await asyncio.sleep(1)

async def closing():
    sales = {"daniel":1500,"Matheus":250,"Marcos":1800}
    invoicing = 1000
    task1 = asyncio.create_task(calculate_bonus_workers(sales))
    task2 = asyncio.create_task(calculateTax(invoicing))
    print("End")
    await task1
    await task2

    #tax = await task2


asyncio.run(closing())

print("-"*30)
print()
print("PROGRAMAÇÃO SÍNCRONA")
print("-"*30)
def calculateTax2(invoicing):
    print(invoicing * 0.1)
    #return invoicing * 0.1


def calculate_bonus_workers2(sales):
    for workers in sales:
        sale = sales[workers]
        print(workers, "bonus", sale * 0.05)
        time.sleep(1)

def closing():
    sales = {"daniel":1500,"Matheus":250,"Marcos":1800}
    invoicing = 1000
    calculate_bonus_workers2(sales)
    calculateTax2(invoicing)
    print("End")
    #tax = await task2

closing()