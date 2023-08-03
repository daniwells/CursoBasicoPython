#n = [2, 5, 4, 2]
#print(n)
#n[2] = 25
#print(n)
#n.append(11)
#print(n)
#n.sort()
#print(n)
#n.sort(reverse=True)
#print(n)
#print(f'Ths list have {len(n)} elements')
#n.insert(1, 45)
#print(n)
#n.insert(5, 3)
#print(n)

##################################################

#n.remove(2)
#print(n)
#n.pop()
#print(n)
#n.pop(3)
#print(n)

##################################################

#if 6 in n:
    #n.remove(6)
#else:
    #print('There is not this element in list!')

##################################################

#values = []

#values.append(5)
#values.append(4)
#values.append(9)

#for c in range(0, 5):
    #values.append(int(input('Type it a value: ')))

#for c, v in enumerate(values):
    #print(f'In position {c} there is the value {v}')
#print('END')

#####################################################

"""a = [1, 4, 5]
b = a
b[1] = 9
print(a)
print(b)"""
# QUANDO SE IGUALA UMA LISTA NO PYTHON, AS LISTAS VÃO ESTAR LIGADAS.

#PARA FAZER UMA CÓPIA DOS VALORES:
"""c = a[:]
print(c)
c[1] = 10
print(c)"""

list = [1, 2, 3]
print(list.index(2))