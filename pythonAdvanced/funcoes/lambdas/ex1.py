"""result = lambda a,b:a+b

print(result(2,5))"""

######################################

"""mult = lambda a,b,c:(a+b)*c

print(mult(2,6,3))"""

######################################

#print((lambda a,b:a+b)(3,5))

######################################


r = lambda x,func:x+func(x)

res = r(2, lambda x:x*x)

print(res)