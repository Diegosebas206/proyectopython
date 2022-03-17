consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Puerto Ayora': { 'consumos': (50, 50),'tarifa': 10}
 },
}

informacion = {
    'Costa': ('Guayaquil', 'Manta'),
    'Sierra': ('Quito', 'Ambato', 'Loja'),
    'Oriente': ('Tena', 'Nueva Loja')
}

informacion['Insular'] = ('Puerto Ayora', 'Puerto Villamil')
#1
def total_consumo_por_zona_lugar(zona, lugar):
    if zona not in consumo_energia.keys():
        return 'La zona ' + zona + ' no existe'

    if lugar not in consumo_energia[zona].keys():
        return 'La zona ' + zona + ' no proveé energía del lugar de ' + lugar 

    total_consumo = sum(consumo_energia[zona][lugar]['consumos'])
    return total_consumo
#2
def total_consumo_lugar(lugar):
      
    if lugar not in consumo_energia['Coca Codo Sinclair'].keys():
        return 'No hay zona de Coca Codo Sinclair en ' + lugar


    total_consumo2 = sum(consumo_energia['Coca Codo Sinclair'][lugar]['consumos'])
    print( 'El consumo de energía de la zona Coca Codo Sinclair en la lugar de',lugar,total_consumo2,"MWh")

def total_consumo_lugar1(lugar):
    if lugar not in consumo_energia['Sopladora'].keys():
        return 'No hay zona de Sopladora en ' + lugar

    total_consumo2 = sum(consumo_energia['Sopladora'][lugar]['consumos'])
    print( 'El consumo de energía de la zona Sopladora en la lugar de',lugar,total_consumo2,"MWh")
#3
def total_por_region(region):
    if region not in informacion.keys():
        return 'region no existe'
        
    lugares_region = informacion[region]
    total_consumo = 0
    for lugar_region in lugares_region:
        for zona in consumo_energia.keys():
            for lugar in consumo_energia[zona].keys():
                if lugar_region ==  lugar:
                    total_consumo += sum(consumo_energia[zona][lugar]['consumos']) * consumo_energia[zona][lugar]['tarifa']

    return total_consumo

op = -1
while op != 0:

    print('<1> Total de energía consumida por zona y lugar')
    print('<2>. Total de Energia por lugar ')
    print('<3>. Dinero Recaudado por Region ')
    print('<0> Salir')

    op = int(input('Ingrese opción:'))
#1. Solicite al usuario el nombre de una zona y de una lugar y presente el total de
#megavatios de consumos para dicha lugar en dicha zona.
    if op == 1:
        print('''
    ===============================
         TOTAL DE MEGAVATIOS
               ZONAS
    Coca Codo Sinclair,Sopladora
    ===============================
    ''')
        zona = input('Ingrese el nombre de la zona:')
        lugar = input('Ingrese el nombre de la lugar:')

        total = total_consumo_por_zona_lugar(zona, lugar)

        if type(total) == int:
            print('El consumo de energía en la lugar de {} fue de {} MWh en la zona {}'.format(lugar, total, zona))
        else:
            print(total)

#2. Solicite al usuario el nombre de una lugar y presente un nuevo diccionario cuyas claves
#son los nombres de las zonass generadoras y el valor es el total megavatios que cada
#zona le ha dado a lugar. Si la zona no entrega energía a la lugar entonces esa zona
#no debería aparecer en el nuevo diccionario  
    elif op == 2:
        print('''
    ===============================
    TOTAL DE ENERGIA DADA A CADA
       LUGARES POR CADA ZONA
               LUGARES
    Guayaquil
    Quito
    Loja
    Ambato
    Tena
    Nueva loja
    Manta
    ===============================
    ''')
        lugar = input('Ingrese el nombre de la lugar:')
        total1 = total_consumo_lugar(lugar)
        total2 = total_consumo_lugar1(lugar)
        if type(total1 and total2)==int:
            print(total1)
            print(total2)
        else:
            print(total1)
            print(total2)
#3. Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la
#región    
    elif op == 3:
        print('''
    ===============================
          DINERO RECAUDADO 
              REGIONES
    Costa
    Sierra
    Oriente
    Insular
    ===============================
    ''')
        region = input('Ingrese región:')
        total = total_por_region(region)
        print("La Region",region, 'es igual:', total,"Dolares$", '\n')
