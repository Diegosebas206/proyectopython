# ¿Qué es Python? 📦  
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.2​ Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.  
Administrado por la Python Software Foundation, posee una licencia de código abierto, denominada Python Software Foundation License.3​ Python se clasifica constantemente como uno de los lenguajes de programación más populares.
# ¿Qué es una variable? 📜  
Una variable se declara para indicarle al programa a partir de qué lugar empieza a existir, qué nombre tendrá y qué tipo de datos almacenará. La asignación de un valor inicial se llama inicialización.  
## Nombrando una variable 📃
```Python 
variable
```
## Asignando valores a una variable 📃
```Python
variable = 100  
varianle = "hola"
```
## Operadores básicos 📃
```Python
suma : +  
resta : -  
multiplicación : *  
división : /  
división entera : //  
módulo : %  
potenciación : **
```
### Suma 1️⃣
```Python
suma = 10 + 10  
    print (suma)
```
### Resta 2️⃣
```Python  
resta = 10 - 10  
    print (resta)
```
### Multiplicación 3️⃣
```Python
multiplicación = 10 * 10  
    print (multiplicación)
```
### División 4️⃣
```Python
división = 10 / 10  
    print (división)
```
### Módulo 5️⃣
```Python
modulo = 10 % 10
    print (mpdulo)
```
### Potencia 6️⃣
```Python
potencia = 10 ** 10
    print (potencia)
```
# Tipos de datos en Python 📜
## Integer 📃
El tipo de datos entero se define por la palabra reservada int. Para definir un tipo de dato, se escribe lo siguiente: int nombre_variable = valor; No es necesario que la variable tenga un valor predeterminado.

ejemplo:
```Python
a = 100  
num = 400
```
## Float 📃
El formato de dato del tipo “coma flotante” o “float” se aplica a los números con decimales.

ejemplo:
```Python
a = 9.2  
num = 10e2
```
## String 📃
El objeto String se utiliza para representar y manipular una secuencia de caracteres que representan un texto.

ejemplo:  
```Python
print("Hola, me llamo Diego")
```
## Casting en Python 📃
Convierte un tipo de datos a otro, pueden ser:  
int  
float  
string

ejemplo:
```Python
num1 = 34   # <class 'int'>  
num2 = 5.99 # <class 'float'>  
a = a + b  
print(a)       # 39.99 
print(type(a)) # <class 'float'>
```
## List 📃
Una lista es una estructura de datos y un tipo de dato en python con características especiales. Lo especial de las listas en Python es que nos permiten almacenar cualquier tipo de valor como enteros, cadenas y hasta otras funciones.

ejemplo:
```Python
lista = [1, 2.5, 'Diego', [5,6] ,4]
```
## Tuple 📃
Un tuple es una colección de datos cuyo orden es inalterable, o sea, son elementos ordenados en una secuencia específica y que posee importancia. En Python, los tuples se escriben entre paréntesis.

ejemplo:
```Python
tuple_frutas = ("manzana", "plátano", "cereza")  
tuple_frutas[3] = "piña" #Esto creará un error  
print(tuple_frutas)
```
## Dictionary 📃
Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento por una clave (Key).

ejemplo:
```Python
diccionario = {'nombre' : 'Diego', 'edad' : 21, 'cursos': ['Python'] }

print diccionario['nombre'] #Diego  
print diccionario['edad']#21  
print diccionario['cursos'] #['Python']
```
# Tomando decisiones 📜
## Sentencia if 📃
La estructura de control if ... permite que un programa ejecute unas instrucciones cuando se cumplan una condición. En inglés "if" significa "si" (condición).

ejemplo:
```Python
m = 10  
if m = 10  
    print('hola')
[salida] = hola
```
## Ciclo For 📃
En general, un bucle es una estructura de control que repite un bloque de instrucciones. Un bucle for es un bucle que repite el bloque de instrucciones un número prederminado de veces. El bloque de instrucciones que se repite se suele llamar cuerpo del bucle y cada repetición se suele llamar iteración.
```Python
print("Comienzo")  
for i in [0, 1, 2]:  
    print("Hola ", end="")  
print()  
print("Final")
```
## Ciclo While 📃
Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True).

ejemplo:
```Python
i = 1  
while i <= 3:  
    print(i)  
    i += 1  
print("Programa terminado")
  ```
## Break 📃:  
En Python, la instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.

ejemplo:
```Python
number = 0

for number in range(10):  
    if number == 5:  
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')
```
## Continue 📃
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.

ejemplo:
```Python
number = 0

for number in range(10):  
    if number == 5:  
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop')
```