#ejemplo 1
numero = 0
print('Tabla del 3')
while numero <= 10:
    print(f'{numero * 3}')
    numero += 1
print('Fin')

#ejemplo 2
valores = [5, 1, 9, 2, 7, 4]
encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista de valores')

#ejemplo 3
valores = [5, 1, 9, 2, 7, 4]
encontrado = False
indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
        break
    else:
        indice += 1
if encontrado:
    print(f'El elemento 2 ha sido encontrado en el índice {indice}')
else:
    print('El elemento 2 no se encuentra en la lista de valores')