#ejemplo 1
h = 0
for i in range(10):
    h += 3
    print('i:', i, 'h:', h)
    if h >= 2 and h <= 36:
        continue
    print('el valor de h:', h)

#ejemplo 2
var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print ("Valor actual de la variable : " + str(var))

print ("fin del script")

#ejemplo 3
for letra in "Python":
    if letra == "h":
        continue
    print ("Letra actual : " + letra)