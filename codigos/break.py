#ejemplo 1
number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')

#ejemplo 2
x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")

#ejemplo 3
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)