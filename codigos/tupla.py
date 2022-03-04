#ejemplo 1
tuple = [23,"Python","Diego",67]
finaltuple = [x for x in zip(*[iter(tuple)])]

print(finaltuple)

#ejemplo 2
tuple = [23,"Python","Diego",26]
finaltuple = [x for x in zip(*[iter(tuple)]*2)]

print(finaltuple)

#ejemplo 3
datos = [(4,3,2),('T','C','S')]

print("Lista: ",datos)