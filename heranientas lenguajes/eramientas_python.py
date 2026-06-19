# operadores numericos
suma = 2 + 2 
print(suma)
resta = 1-2 
print(resta)
multiplicacion = 2 * 2 
print(multiplicacion)
divicion = 2 / 1 
print(divicion)


 
# los parentecis me cirven para agrupar
suma1 = (2+2/2)*1 # Se pueden convinar todos los operadores numericos
print(suma1)
divicion1 = 2 // 2 # Me ayuda a ovtener un numero entero de una divicion 
print(divicion1)

divicion2 = 2 % 2
print(divicion2)

# Calculo de potenciales o elevados 
poteciales = 2 ** 2
print(poteciales)

# salto de linea
tex = "hola \nene" # salto de linea
print(tex) # La letra (r) me ayuda a que no se ejecute el salto de linea
# Salto de tabla 
Tax = "hola \tpedro"
print(Tax)
# Salto de retorno
Tux = " hola\rnene " # No me meuestra la primera palabra ingresada amenos que se muestran dos palabras antes y me mosrara la segunda ingresada 
print(Tux)
# subindices es decir me dice a cuantas casillas esta una letra de la otra
word = 'Python'
mensaje = word[0]
print(mensaje)

mensaje = word[0:3]# Tambien funciona de forma negativa 
print(mensaje)

# La funcion len() me ayuda asever la longuitud de una palabra o la cantidad e letras que tenga una palabra incliyendo espacios
palo = 'perro lo'
mensaje = len(palo)
print(mensaje)

# Los estring 
Pepe = str(5)
print(Pepe)

# list() me ayuda a convertir una cadena de texto en una lista.
nombre = "santiago"
print(list(nombre))






# LISTAS

# Listas la lista se representa con : list o []
Numero = [ 1,2,3,4,5]
# append mecirve para agregar un objeto al final de una     lista 
Numero.append(6)
print(Numero)

numero_max = max(Numero) # max me ayuda a obtener el numero mayor de una lista
print(numero_max)   

numero_min = min(Numero) # min me ayuda a obtener el numero menor de una lista
print(numero_min)

suma_lista = sum(Numero) # sum me ayuda a obtener la suma de los elementos de una lista
print(suma_lista)

sorted_lista = sorted(Numero) # sorted me ayuda a ordenar una lista de menor a mayor sin modificar la lista original
print(sorted_lista)

sorted_lista_desc = sorted(Numero, reverse=True) # reverse=True me ayuda a ordenar una lista de mayor a menor sin modificar la lista original
print(sorted_lista_desc)

palabras = ["manzana", "banana", "cereza"]
sorted_palabras = sorted(palabras) # sorted me ayuda a ordenar una lista de palabras de a-z sin modificar la lista original

sorted_orde_palabras = sorted(palabras, reverse=True) # reverse=True me ayuda a ordenar una lista de palabras de z-a sin modificar la lista original
print(sorted_palabras)

orden_palabras_cantidad = sorted(palabras, key=len) # key=len me ayuda a ordenar una lista de palabras por la cantidad de letras sin modificar la lista original
print(orden_palabras_cantidad)

# verificasion si una lista tiene x numeros o tiene mas de x numeros
if len(Numero) > 3:
    print("La lista tiene mas de 3 numeros")

Numero1 = [ 1,2,3,4,5]
#remove me cirve para eliminar un objeto de la lista
Numero1.remove(4)
print(Numero1)
Numero1.clear() # clear me ayuda a eliminar toda la lista
print(Numero1)
#pop me ayuda a eliminir un elemento por medio de indices 
Numero1 = Numero1.pop(1)
print(Numero1)
Numero2 = [ 1,2,3,4,5]
# len me imprime la longuitud de la lista   
print(len(Numero2))

Numero1.reverse() # reverse me ayuda a invertir el orden de la lista
print(Numero1)
Numero2 = [ 2,1,4,5,3]  
# sort me ordena la lista de a-z o de numero menor a mayor
Numero2.sort()
print(Numero2)

Agregar = [int(input("Agrega el numero")), int(input("Agrega el segundo dato"))]
print(Agregar)

# Funcion match me cirve para realisar comparaciones de patrones y ejecutar codigo especifico segun el patron que se ejecuta 
Dato1, Dato2 = int(input("Ingresa el primer dato")), int(input("Ingresa el seundo dato"))
 
operador = input("ingresa la operacion (+ - * / ): ")

match operador:
    case "+":
        res = Dato1+Dato2
    case "-":
        res = Dato1-Dato2
    case "*":
        res = Dato1*Dato2
    case "/":
        res = Dato1/Dato2
 
print(f"El resultado de {Dato1} {operador} {Dato2} = {res}")     

# upper me ayuda aponer unapalabra en mayuscula
cater = "santiago"
mayuscula = cater.upper()
print(mayuscula)

#lower Me ayuda aponer una palabra en minuscula 
nom2 = "PEDRO" 
respuesta = nom2.lower()
print(respuesta)
 # capitañize Me ayuda a poner la primera letra de una palabra en mayuscula
res = nom2.capitalize()
print (res )
# title Me ayuda a ponerle a toda una frase la primera letra de cada palabra en mayuscula 
resp = nom2.title()
print(resp)

# while es un bucle que me permite sumar el primer numero con el anterior 
# end  me ayuda a que no se salte de linea y se muestre todo en una sola linea
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a+b

#for es un bucle que me permite repetir una palabra las beses q yo quiera  o un numero del 0 asta el numero indicado 
for i in range(2):
    print("HILA")

for i in range(10):
    print(i)

# El bucle while ejecuta un bloque de código una y otra vez mientras una condición sea verdadera.

gritos = 10 # Se le asigna un valor a la variable gritos
while gritos > 0: # Mientras la variable gritos sea mayor a 0 se ejecutara el codigo
 print(gritos) # Se imprime el valor de la variable gritos
 gritos = gritos - 1 # Se le resta 1 a la variable gritos o el numero q desiemos 




'''// FUNCIONES \\'''
#  * me sirve para que la funcion reciva todos los argumentos que yo quiera y los guarde en una tupla con el nombre que yo le asigne a la variable
def sumas(*suma):

    resultado = 0
    for numero in suma:
        resultado += numero
    return resultado

sumas(1, 2, 3, 4) # Se llama a la función sumas con varios argumentos, lo que permite calcular la suma de esos números y devolver el resultado. En este caso, se sumarán los números 1, 2, 3 y 4, y se devolverá el resultado que es 10.


# ** me sirve para que la funcion reciva todos los argumentos que yo quiera y los guarde en un diccionario con el nombre que yo le asigne a la variable

def informacion(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

informacion(nombre="Santiago", edad=25, ciudad="Buenos Aires") # Se llama a la función informacion con argumentos de palabras clave, lo que permite imprimir la información proporcionada en un formato legible.


# def en es una palabra clave utilizada para definir funciones. Las funciones te permiten agrupar bloques de código que realizan una tarea específica, lo que facilita su reutilización y organización.

def saludar(nombre): # Se define la funcion saludar con un parametro nombre
    print("Hila" + nombre) # Se imprime el saludo con el nombre proporcionado

#retornacion de multiples valores de una funcion
def operaciones():
    return "suma", "resta", "multiplicacion", "divicion" # Se retorna una tupla con los resultados de las operaciones

retorno_suma, retorno_resta, retorno_multiplicacion, retorno_divicion = operaciones() # Se asignan los valores retornados por la funcion a variables individuales

print(retorno_suma) # Se imprime el resultado de la suma
print(retorno_resta) # Se imprime el resultado de la resta
print(retorno_multiplicacion) # Se imprime el resultado de la multiplicacion



# Funcion lambda es una función anónima que se utiliza para crear funciones pequeñas y simples de una sola línea. Se define utilizando la palabra clave lambda seguida de los parámetros y el cuerpo de la función.
suma_lambda = lambda x, y: x + y # Se define una función lambda para sumar dos números, donde x e y son los parámetros de entrada y x + y es el resultado que se devuelve.

resultado = suma_lambda(5, 3) # Se llama a la función lambda con los argumentos 5 y 3, y se almacena el resultado en la variable resultado.

print(resultado) # Se imprime el resultado de la suma, que en este caso sería 8

# sorted me ayuda a ordenar una lista de acuerdo a una clave especifica utilizando una funcion lambda como clave de ordenamiento
names = ["Alice", "Bob", "Charlie", "Diana"]
return_names = sorted(names, key=lambda name: len(name)) # Se utiliza la función sorted para ordenar la lista de nombres según la longitud de cada nombre, utilizando una función lambda como clave de ordenamiento.

#Ordenar tuplas por múltiples criterios:
data = [("Alice", 25), ("Bob", 30), ("Charlie", 25)]
sorted_data = sorted(data, key=lambda x: (x[1], x[0])) # Se utiliza la función sorted para ordenar la lista de tuplas data primero por la edad (x[1]) y luego por el nombre (x[0]) en caso de que haya edades iguales, utilizando una función lambda como clave de ordenamiento.
print(sorted_data) # Se utiliza la función sorted para ordenar la lista de tuplas data primero por la edad (x[1]) y luego por el nombre (x[0]) en caso de que haya edades iguales, utilizando una función lambda como clave de ordenamiento.

#Ordenar números por valor absoluto:
numbers = [-10, 15, -20, 25]
sorted_numbers = sorted(numbers, key=lambda x: abs(x)) #sorted me ayuda a ordenar una lista de números según su valor absoluto, utilizando una función lambda como clave de ordenamiento. Esto significa que los números se ordenarán en función de su distancia desde cero, sin importar si son positivos o negativos.
print(sorted_numbers) # Se utiliza la función sorted para ordenar la lista de números según su valor absoluto, utilizando una función lambda como clave de ordenamiento. Esto significa que los números se ordenarán en función de su distancia desde cero, sin importar si son positivos o negativos.

#Ordenar diccionarios por valores:
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
sorted_grades = sorted(grades.items(), key=lambda x: x[1]) # Se utiliza la función sorted para ordenar los elementos del diccionario grades por sus valores (calificaciones), utilizando una función lambda como clave de ordenamiento. Esto devuelve una lista de tuplas ordenada por las calificaciones de menor a mayor.
print(sorted_grades) # Se utiliza la función sorted para ordenar los elementos del diccionario grades por sus valores (calificaciones), utilizando una función lambda como clave de ordenamiento. Esto devuelve una lista de tuplas ordenada por las calificaciones de menor a mayor.

#Ordenar cadenas por longitud:
names = ["Alice", "Bob", "Charlie", "Diana"]
sorted_names = sorted(names, key=lambda x: len(x)) # Se utiliza la función sorted para ordenar la lista de nombres según la longitud de cada nombre, utilizando una función lambda como clave de ordenamiento. Esto devuelve una lista de nombres ordenada de menor a mayor longitud.
print(sorted_names) # Se utiliza la función sorted para ordenar la lista de nombres según la longitud de cada nombre, utilizando una función lambda como clave de ordenamiento. Esto devuelve una lista de nombres ordenada de menor a mayor longitud.

# Funciones Recursivas
def factorial(n): # Se define la función factorial que toma un número n como argumento
    if n == 0: # Caso base: si n es igual a 0, el factorial es 1
        return 1
    else: # Caso recursivo: si n es mayor que 0, se llama a la función factorial con n-1 y se multiplica por n
        return n * factorial(n - 1)
print(factorial(5)) # Se llama a la función factorial con el argumento 5, lo que calculará el factorial de 5 (5 * 4 * 3 * 2 * 1) y se imprimirá el resultado, que es 120.

 # Ejemplo de función recursiva para invertir una cadena de texto
def recursive_reverse(s): # Se define la función recursive_reverse que toma una cadena de texto s como argumento
    if len(s) <= 1:  # Caso base: cadena vacía o de un solo carácter
        return s # Si la longitud de la cadena es menor o igual a 1, se devuelve la cadena tal cual, ya que no hay nada que invertir.
    
    else: # Caso recursivo: se toma el primer carácter de la cadena y se coloca al final, luego se llama a la función recursive_reverse con el resto de la cadena (s[1:]) y se concatena con el primer carácter (s[0]).
        return recursive_reverse(s[1:]) + s[0]  # Paso recursivo

text = "hello" # Se define la cadena de texto "hello" que se desea invertir utilizando la función recursiva.
result = recursive_reverse(text) # Se llama a la función recursive_reverse con la cadena "hello", lo que invertirá la cadena y se almacenará el resultado en la variable result. Luego, se imprime el resultado, que será "olleh".
print(result)

# funcion de un reloj digital
import tkinter as tk
from time import strftime

# Crear la ventana principal
root = tk.Tk()
root.title("Reloj Digital")

# Configurar el texto del reloj
def actualizar_reloj():
    hora_actual = strftime('%H:%M:%S')
    etiqueta_hora.config(text=hora_actual)
    etiqueta_hora.after(1000, actualizar_reloj)  # Actualizar cada segundo

etiqueta_hora = tk.Label(root, font=('Arial', 48), bg='black', fg='white')
etiqueta_hora.pack(expand=True, fill='both')

# Inicializar el reloj
actualizar_reloj()
root.mainloop()






'''// BUCLES \\ '''

#isinstance es una función integrada en Python que sirve para verificar si un objeto pertenece a un tipo de dato específico.

for i in range(5):
    if isinstance(i, int): # Se verifica si el valor de i es un entero
        print(f"{i} es un número entero.") # Si i es un entero se imprime el mensaje indicando que es un número entero
    else:
        print(f"{i} no es un número entero.") # Si i no es un entero se imprime el mensaje indicando que no es un número entero

for i in range(5):
    if i % 2 == 0: # Se verifica si el valor de i es par (es decir, si el resto de la división entre i y 2 es igual a 0)
        print(f"{i} es un número par.") # Si i es par se imprime el mensaje indicando que es un número par
        continue  # es una palabra clave utilizada dentro de los bucles (como for o while) para saltar a la siguiente iteración del bucle sin ejecutar el código restante en la iteración actual.
    
    else:
        print(f"{i} es un número impar.") # Si i no es par se imprime el mensaje indicando que es un número impar   
    
lista = [1, 2, 3, 4, 5]

# bucle de  ejemplo de comprensión de listas 

nueva_lista = [n * 3 for n in lista] # Esta es una forma de crear una nueva lista a partir de otra lista utilizando una comprensión de listas. En este caso, se multiplica cada elemento de la lista original por 3 y se guarda en la nueva lista.
print(nueva_lista)

# bucle de comprension de listas con condicion
nueva_lista_condicional = [n * 3 for n in lista if n % 2 == 0] # Esta es una forma de crear una nueva lista a partir de otra lista utilizando una comprensión de listas con una condición. En este caso, se multiplica cada elemento de la lista original por 3 solo si el elemento es par (es decir, si el resto de la división entre el elemento y 2 es igual a 0).
print(nueva_lista_condicional)

#La función abs() en Python devuelve el valor absoluto de un número.
print(abs(-5)) # Devuelve 5

numero_absolut = [-1, -2, -3, 4, 5]

# Ejemplo de uso de abs() con una lista de números
valores_absolutos = [abs(n) for n in numero_absolut] # Esta es una forma de crear una nueva lista a partir de otra lista utilizando una comprensión de listas y la función abs(). En este caso, se obtiene el valor absoluto de cada elemento de la lista original y se guarda en la nueva lista.
print(valores_absolutos)

suma = 0
for i in range(len(lista)):
    suma += lista[i]
print(suma)

# Otra forma de hacer lo mismo usando un bucle for directamente sobre los elementos de la lista el ual nos ayuda a recorer los elementos de lalista 1 por 1
suma = 0
for numero in lista:
    suma += numero

print(suma)

print(round(3.14159, 2))  # Redondear a 2 decimales # round me ayuda a redondear un numero a la cantidad de decimales que yo quiera

# {} con las llaves puedo crear un diccionario
#ejemplo de uso de diccionario  
mi_diccionario = {
    "nombre": "Santiago",
    "edad": 25,
    "ciudad": "Bogotá"
}
print(mi_diccionario)



# DICIIONARIOS
# Ejemplo de creacion de un diciionario y acceso a sus elementos

personas = {
    "Juan": {"edad": 30, "ciudad": "Madrid"},
    "Ana": {"edad": 25, "ciudad": "Barcelona"},
    "Luis": {"edad": 28, "ciudad": "Valencia"}
}
#Ejemplo de como adcceder a los elementos del diccionario
print(personas)

#Forma de acceso por elemento
print(personas("Juan"))

# Forma de acceso por elemento especifico
print(personas["Ana"]["ciudad"])

#Forma de adcceder por forma de bicle for
for nombre, info in personas.items(): # items me ayuda a recorrer los elementos de un diccionario
    print(f"{nombre} tiene {info['edad']} años y vive en {info['ciudad']}.")

# Agrega un nuevo elemento al diccionario
personas["Marta"] = {"edad": 22, "ciudad": "Sevilla"}
print(personas)

# Eliminar un elemento del diccionario
del personas["Luis"]    
print(personas)

# Verificar si una clave existe en el diccionario
if "Ana" in personas:
    print("Ana está en el diccionario.")

# Obtener todas las claves del diccionario
claves = personas.keys() # keys me ayuda a obtener todas las claves de un diccionario
print(claves)

# Obtener todos los valores del diccionario
valores = personas.values() # values me ayuda a obtener todos los valores de un diccionario
print(valores)

age = personas.get("Juan", {}).get("edad") # get me ayuda a obtener el valor de una clave especifica en un diccionario
print(age)

cyty = personas.pop("Ana", {}).get("ciudad") # pop me ayuda a eliminar un elemento de un diccionario y obtener su valor
print(cyty)





# CONJUNTOS


# Los conjuntos en Python son colecciones desordenadas de elementos únicos. Se definen utilizando llaves {} o la función set() para crear conjuntos vacios. Los conjuntos son útiles para realizar operaciones matemáticas como unión, intersección y diferencia.   
# Ejemplo de creacion de un conjunto y operaciones basicas
conjunto_a = {1, 2, 3, 4, 5}
print(conjunto_a)
lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10]
# creacion de un conjunto vacio
conjunto_b = set() 
print(conjunto_b)

# set tambien me sirve para comvertir una lista en un conjunto y
conjunto_b = set(lista_a)
print(conjunto_b)

# Como agrear un ele,ento en un conjunto
conjunto_a.add(6) # .add me ayuda a agregar un elemento a un conjunto
print(conjunto_a)

# Como eliminar un elemento de un conjunto
conjunto_a.remove(3) # .remove me ayuda a eliminar un elemento de un conjunto. Si el elemento no existe genera un error.

conjunto_a.discard # .discard me ayuda a eliminar un elemento de un conjunto. Si el elemento no existe no genera un error. 
print(conjunto_a)

conjunto_a.pop() # .pop me ayuda a eliminar un elemento aleatorio de un conjunto y devolverlo. Si el conjunto esta vacio genera un error.
print(conjunto_a)   

conjunto_a.clear() # .clear me ayuda a eliminar todos los elementos de un conjunto
print(conjunto_a)

con_1 = {1, 2, 3}
con_2 = {3, 4, 5}
union_con = con_1.union(con_2) # .union me ayuda a obtener la union de dos conjuntos excluyendo los elementos repetidos
print(union_con) 

union_con = con_1 | con_2 # Otra forma de obtener la union de dos conjuntos utilizando el operador |
print(union_con)


conmun_con = con_1.intersection(con_2) # .intersection me ayuda a obtener la interseccion de dos conjuntos es decir los elementos que se repiten en ambos conjuntos
print(conmun_con)

conmun_con = con_1 & con_2 # Otra forma de obtener la interseccion de dos conjuntos utilizando el operador &
print(conmun_con)


diference_con = con_1.difference(con_2) # .difference me ayuda a obtener la diferencia de dos conjuntos es decir los elementos que estan en el primer conjunto pero no en el segundo
print(diference_con)

diference_con = con_1 - con_2 # Otra forma de obtener la diferencia de dos conjuntos utilizando el operador -
print(diference_con)

diferencia_con = con_1.symmetric_difference(con_2) # .symmetric_difference me ayuda a obtener la diferencia simetrica de dos conjuntos es decir los elementos que estan en ambos conjuntos pero no en ambos al mismo tiempo
print(diferencia_con)   

diference_con = con_1 ^ con_2 # Otra forma de obtener la diferencia simetrica de dos conjuntos utilizando el operador ^
print(diference_con)

# Verificacion de subconjunto
verificasio_sub = con_1 <= con_2 # El operador <= me ayuda a verificar si un conjunto es subconjunto de otro
print(verificasio_sub)

# verificacion de superconjunto propio 
verificasio_sub = con_1 < con_2 # El operador < me ayuda a verificar si un conjunto es subconjunto propio de otro
print(verificasio_sub)

# verificacion de un super conjunto
verificasio_super = con_1 >= con_2 # El operador >= me ayuda a verificar si un conjunto es superconjunto de otro
print(verificasio_super)

# verificacion de super conjunto propio
verificasio_super = con_1 > con_2 # El operador > me ayuda a verificar si un conjunto es superconjunto propio de otro
print(verificasio_super)    



'''// CLASES \\'''
# class es una palabra clave utilizada para definir una clase en Python. Las clases son plantillas para crear objetos y encapsulan datos y comportamientos relacionados.

class Persona: # Se define la clase Persona
    def __init__(self, nombre, edad): # El método __init__ es el constructor de la clase, que se ejecuta automáticamente al crear una instancia de la clase. En este caso, toma dos parámetros (nombre y edad) y los asigna a los atributos de la instancia.
        self.nombre = nombre # Se asigna el valor del parámetro nombre al atributo nombre de la instancia
        self.edad = edad # Se asigna el valor del parámetro edad al atributo edad de la instancia

    def saludar(self): # Se define un método llamado saludar dentro de la clase Persona. Este método no toma parámetros adicionales y se utiliza para imprimir un saludo personalizado utilizando el atributo nombre de la instancia.
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.") # Se imprime un mensaje de saludo que incluye el nombre y la edad de la persona utilizando una f-string para formatear el texto.


'''Datetime: Permite trabajar con fechas y horas, como datetime.now() (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.'''


''' // modulos integrados \\'''

import math # math me ayuda a realizar operaciones matematicas como raiz cuadrada, potencia, logaritmo, etc.

'''Proporciona funciones matemáticas, como sqrt() (raíz cuadrada), sin() (seno), cos() (coseno), entre otras.'''

resultado = math.sqrt(25) # sqrt me ayuda a obtener la raiz cuadrada de un numero. En este caso, se obtiene la raiz cuadrada de 25, que es 5.0.
print(resultado)  # Imprime 5.0


# Importacion de funciones especificas de un modulo
from math import sqrt # from me ayuda a importar una función específica de un módulo. En este caso, se importa la función sqrt del módulo math, lo que permite usar sqrt directamente sin tener que escribir math.sqrt cada vez.

resultado = sqrt(25) #
print(resultado)  # Imprime 5.0


#import me ayuda a importar una libreria o modulo para utilizar sus funciones o clases

import random # random me ayuda a generar numeros aleatorios

'''Ofrece funciones para generar números aleatorios, como random() (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras'''

veces = 5
for i  in range(veces):
    numero_aleatorio = random.randint(1, 10) # randint me ayuda a generar un numero aleatorio entre el rango indicado
    print(numero_aleatorio)

     #Propiedades de random

numero_aleatorio = random.randint(a, b) #devuelve un número entero aleatorio N tal que a <= N <= b. Es decir, incluye ambos extremos del rango especificado. Por ejemplo, random.randint(1, 10) puede devolver cualquier número entero entre 1 y 10, incluyendo el 1 y el 10.

numeros_aleatorios_flotantes = random.uniform(a, b) #devuelve un número flotante aleatorio N tal que a <= N <= b. Es decir, incluye ambos extremos del rango especificado. Por ejemplo, random.uniform(1.0, 10.0) puede devolver cualquier número flotante entre 1.0 y 10.0, incluyendo el 1.0 y el 10.0.

numnero_aleatorio_flotante_entre_1_y_0 = random.random() #devuelve un número flotante aleatorio N tal que 0.0 <= N < 1.0. Es decir, incluye el 0.0 pero no incluye el 1.0. Por ejemplo, random.random() puede devolver cualquier número flotante entre 0.0 y 1.0, incluyendo el 0.0 pero excluyendo el 1.0.

elemento_aleatorio_de_una_lista = random.choice(lista) #devuelve un elemento aleatorio de una secuencia no vacía, como una lista o una tupla. Por ejemplo, si tienes una lista llamada mi_lista = [1, 2, 3, 4, 5], entonces random.choice(mi_lista) puede devolver cualquiera de los elementos de la lista, como 1, 2, 3, 4 o 5.

mesclar_aleatoriamente_una_lista = random.shuffle(lista) #mezcla los elementos de una lista de forma aleatoria. Por ejemplo, si tienes una lista llamada mi_lista = [1, 2, 3, 4, 5], entonces random.shuffle(mi_lista) mezclará los elementos de la lista en un orden aleatorio, como [3, 1, 5, 2, 4]. Ten en cuenta que esta función modifica la lista original y no devuelve una nueva lista mezclada.

elementos_sin_repetir = random.sample(lista, 2) #devuelve una lista de k elementos únicos seleccionados aleatoriamente de la secuencia dada. Por ejemplo, si tienes una lista llamada mi_lista = [1, 2, 3, 4, 5] y quieres seleccionar 3 elementos únicos al azar, puedes usar random.sample(mi_lista, 3), lo que podría devolver una lista como [2, 5, 1]. Ten en cuenta que el valor de k debe ser menor o igual al tamaño de la secuencia para evitar un error.


'''// Creacion de modulos personalizados \\'''
# Para crear un módulo personalizado en Python, simplemente necesitas crear un archivo con extensión .py y definir tus funciones, clases o variables dentro de ese archivo. Luego, puedes importar ese módulo en otros archivos de tu proyecto para utilizar sus funcionalidades.

# (mi_modulo.py) es el nombre de la carpeta y el archivo donde se encuentra el modulo personalizado que contiene las funciones saludar y calcular_suma. Estas funciones pueden ser importadas y utilizadas en otros archivos de tu proyecto para realizar tareas específicas, como saludar a un usuario o calcular la suma de dos números.
def saludar(nombre):
    print(f"Hola, {nombre}!")


def calcular_suma(a, b):
    return a + b


# Importacion de un modulo personalizado

'''import mi_modulo''' # import me ayuda a importar un modulo personalizado para utilizar sus funciones o clases. En este caso, se importa el módulo mi_modulo, lo que permite acceder a las funciones definidas en ese módulo utilizando la sintaxis mi_modulo.funcion().

'''
mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8
'''




'''// Creacion de paquetes personalizados \\'''


# Un paquete en Python es una forma de organizar módulos relacionados en una estructura de directorios. Para crear un paquete personalizado, debes seguir estos pasos:
'''
mi_paquete/ # El nombre de la carpeta que representa el paquete
    __init__.py # El archivo __init__.py es necesario para que Python reconozca la carpeta como un paquete. Puede estar vacío o contener código de inicialización para el paquete.
    modulo1.py
    modulo2.py # Dentro de cada módulo, puedes definir tus funciones, clases o variables como lo harías normalmente. Luego, puedes importar estos módulos desde otros archivos de tu proyecto utilizando la sintaxis from mi_paquete import modulo1 o import mi_paquete.modulo1, dependiendo de cómo quieras acceder a las funciones dentro del módulo.
'''
# Importacion de un paquete personalizado
'''
from mi_paquete import modulo1, modulo2 # from me ayuda a importar un modulo especifico de un paquete personalizado para utilizar sus funciones o clases. En este caso, se importan los módulos modulo1 y modulo2 del paquete mi_paquete, lo que permite acceder a las funciones definidas en esos módulos utilizando la sintaxis modulo1.funcion() o modulo2.funcion().

modulo1.funcion1() # Se llama a la función funcion1 del módulo modulo1, lo que ejecutará el código definido en esa función.
modulo2.funcion2()
'''




'''// DETECTOR DE ERRORES\\'''

try: # El bloque try se utiliza para envolver el código que puede generar una excepción. Si se produce una excepción dentro del bloque try, el programa no se detendrá, sino que se ejecutará el bloque except correspondiente.
     
    numero = int(input("Ingresa un número: ")) # Se solicita al usuario que ingrese un número y se intenta convertirlo a un entero. Si el usuario ingresa algo que no se puede convertir a un entero, se generará una excepción ValueError.
    
except ValueError: # El bloque except se ejecuta si se genera una excepción del tipo ValueError. En este caso, se captura la excepción y se ejecuta el código dentro del bloque except.
    print("¡Error! Por favor, ingresa un número válido.") # Si se genera una excepción ValueError, se ejecutará este bloque except y se imprimirá un mensaje de error indicando que el usuario debe ingresar un número válido.

# ValueError es una excepción que se genera cuando se intenta convertir un valor a un tipo de dato específico y la conversión no es posible. En este caso, si el usuario ingresa algo que no se puede convertir a un entero, se generará una excepción ValueError. 
try:
    bocal = str(input("Ingresa una palabra: ")) # Se solicita al usuario que ingrese una palabra y se intenta convertirla a una cadena de texto. Si el usuario ingresa algo que no se puede convertir a una cadena de texto, se generará una excepción ValueError.

except ValueError: # ValueError es una excepción que se genera cuando se intenta convertir un valor a un tipo de dato específico y la conversión no es posible. En este caso, si el usuario ingresa algo que no se puede convertir a una cadena de texto, se generará una excepción ValueError.

    print("¡Error! Por favor, ingresa una palabra válida.") # Si se genera una excepción ValueError, se ejecutará este bloque except y se imprimirá un mensaje de error indicando que el usuario debe ingresar una palabra válida.


# TypeError es una excepción que se genera cuando se intenta realizar una operación o función en un tipo de dato que no es compatible. Por ejemplo, si intentas sumar un número entero con una cadena de texto, se generará una excepción TypeError porque no se pueden sumar tipos de datos diferentes.
try:
    resultado = 5 + "hola" # Se intenta sumar un número entero con una cadena de texto, lo que generará una excepción TypeError.

except TypeError: # El bloque except se ejecuta si se genera una excepción del tipo TypeError. En este caso, se captura la excepción y se ejecuta el código dentro del bloque except.

    print("¡Error! No se pueden sumar tipos de datos diferentes.") # Si se genera una excepción TypeError, se ejecutará este bloque except y se imprimirá un mensaje de error indicando que no se pueden sumar tipos de datos diferentes.


# IOError es una excepción que se genera cuando ocurre un error de entrada/salida, como intentar abrir un archivo que no existe o no tener permisos para acceder a un archivo. Por ejemplo, si intentas abrir un archivo que no existe utilizando la función open(), se generará una excepción IOError.

try:
    with open("archivo_inexistente.txt", "r") as archivo: # Se intenta abrir un archivo que no existe, lo que generará una excepción IOError.
        contenido = archivo.read() # Si el archivo se abre correctamente, se lee su contenido.

except IOError: # El bloque except se ejecuta si se genera una excepción del tipo IOError. En este caso, se captura la excepción y se ejecuta el código dentro del bloque except.

    print("¡Error! No se pudo abrir el archivo.") # Si se genera una excepción IOError, se ejecutará este bloque except y se imprimirá un mensaje de error indicando que no se pudo abrir el archivo.


# ZeroDivisionError es una excepción que se genera cuando se intenta dividir un número por cero. Por ejemplo, si intentas dividir 10 entre 0, se generará una excepción ZeroDivisionError porque la división por cero no está definida matemáticamente.
try:    
    resultado = 10 / 0 # Se intenta dividir 10 entre 0, lo que generará una excepción ZeroDivisionError.
    
except ZeroDivisionError: # El bloque except se ejecuta si se genera una excepción del tipo ZeroDivisionError. En este caso, se captura la excepción y se ejecuta el código dentro del bloque except.

    print("¡Error! No se puede dividir por cero.") # Si se genera una excepción ZeroDivisionError, se ejecutará este bloque except y se imprimirá un mensaje de error indicando que no se puede dividir por cero.



# me sirve para manejar excepciones y asegurar que ciertos recursos se liberen o ciertas acciones se realicen sin importar si ocurre una excepción o no. Por ejemplo, al trabajar con archivos, es importante asegurarse de que el archivo se cierre correctamente incluso si ocurre un error durante la lectura o escritura del archivo. El bloque finally garantiza que el archivo se cierre adecuadamente, evitando posibles fugas de recursos o bloqueos de archivos.
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally: # finally me ayuda a asegurar que ciertos recursos se liberen o ciertas acciones se realicen sin importar si ocurre una excepción o no. En este caso, se asegura de que el archivo se cierre correctamente incluso si ocurre un error durante la lectura del archivo.

    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción  


# lector de archibos 
                             # la letra "r" me ayuda a abrir un archivo en el modo de lectura, lo que significa que solo se puede leer el contenido del archivo y no se pueden realizar modificaciones en él. Si el archivo no existe, se generará un error.|
archivo = open("datos.txt", "r") # open me ayuda a abrir un archibo en el modelo de lectura.
                    # "datos.txt" es el nombre del archivo que se desea abrir. Debe estar en el mismo directorio que el script de Python o proporcionar la ruta completa al archivo.
contenido = archivo.read()# read me ayuda a leer el contenido de un archivo y devolverlo como una cadena de texto. En este caso, se lee todo el contenido del archivo "datos.txt" y se almacena en la variable contenido.
print(contenido)
archivo.close() # close me ayuda a cerrar un archivo después de haberlo utilizado para liberar los recursos asociados con él. Es importante cerrar los archivos después de usarlos para evitar posibles fugas de recursos o bloqueos de archivos.


# E scritura de archivos

archivo = open("datos.txt", "w") # la letra "w" me ayuda a abrir un archivo en el modo de escritura, lo que significa que se puede escribir contenido en el archivo. Si el archivo ya existe, se sobrescribirá su contenido. Si el archivo no existe, se creará uno nuevo.
archivo.write("Hola, mundo!") # write me ayuda a escribir contenido en un archivo. En este caso, se escribe la cadena "Hola, mundo!" en el archivo "datos.txt". Si el archivo ya tiene contenido, este se sobrescribirá con el nuevo contenido.
archivo.close() # close me ayuda a cerrar un archivo después de haberlo utilizado para liberar los recursos asociados con él. Es importante cerrar los archivos después de usarlos para evitar posibles fugas de recursos o bloqueos de archivos.

# Cierre de archibo     
with open("datos.txt", "r") as archivo: # La declaración with se utiliza para manejar recursos de manera eficiente, como archivos. En este caso, se abre el archivo "datos.txt" en modo de lectura ("r") y se asigna a la variable archivo. El bloque de código dentro del with se ejecutará con el archivo abierto, y una vez que se complete el bloque, el archivo se cerrará automáticamente, incluso si ocurre una excepción durante la ejecución del bloque.
    contenido = archivo.read()
    print(contenido)




''' //Como guardadtos con JSON\\'''

import json
 
 # Escribir o agregar datos a un archivo JSON
'''
 with open( "datos_usuario.json", "w") as archivo: # Se abre un archivo llamado "datos_usuario.json" en modo de escritura ("w") utilizando la declaración with, lo que garantiza que el archivo se cerrará automáticamente después de su uso. El archivo se asigna a la variable archivo para su manipulación dentro del bloque with.
        json.dump(usuario, archivo) # json.dump me ayuda a escribir un objeto de Python (en este caso, el diccionario usuario) en un archivo JSON. En este caso, se escribe el contenido del diccionario usuario en el archivo "datos_usuario.json" utilizando la variable archivo como destino.
'''
# Leer datos de un archivo JSON
with open("datos_usuario.json", "r") as archivo: # Se abre el archivo "datos_usuario.json" en modo de lectura ("r") utilizando la declaración with, lo que garantiza que el archivo se cerrará automáticamente después de su uso. El archivo se asigna a la variable archivo para su manipulación dentro del bloque with.
             usuario =  json.load(archivo) # json.load me ayuda a leer el contenido de un archivo JSON y convertirlo en un objeto de Python. En este caso, se lee el contenido del archivo "datos_usuario.json" utilizando la variable archivo como fuente y se almacena en la variable usuario como un diccionario de Python.
print(usuario) # Se imprime el contenido del diccionario usuario, que contiene los datos leídos del archivo JSON.





'''  //Importacion de archivos\\ '''

# Archivo"usuario.py"

class Usuario:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def mostrar_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")


# Archivo "main.py"

#from usuario import Usuario # from me ayuda a importar una clase específica de un módulo personalizado para utilizarla en otro archivo. En este caso, se importa la clase Usuario del módulo usuario, lo que permite crear instancias de la clase Usuario y acceder a sus métodos y atributos utilizando la sintaxis Usuario().

usuario1 = Usuario("Santiago", 17, "santiago@gmail.com")

usuario1.mostrar_usuario()


#Archivo "admin.py" con importacion de paquete personalizado

#from usuario import Usuario # from me ayuda a importar una clase específica de un módulo personalizado para utilizarla en otro archivo. En este caso, se importa la clase Usuario del módulo usuario, lo que permite crear instancias de la clase Usuario y acceder a sus métodos y atributos utilizando la sintaxis Usuario().

class Admin(Usuario):

    def mostrar_permiso(self):
        print("El permiso fue agregado correctamente")

    def mostrar_negacion(self):
        print("El permiso fue denegado")

admin1 = Admin("Sharo", 16, "sharo@gmail.com")
admin1.mostrar_negacion()
admin1.mostrar_permiso()




'''// Creacion de API con FastAPI\\'''
from fastapi import FastAPI # FastAPI es un framework web moderno y rápido para construir APIs con Python. Proporciona una forma sencilla de crear endpoints y manejar solicitudes HTTP, lo que facilita el desarrollo de aplicaciones web y servicios RESTful.


app = FastAPI() # Se crea una instancia de la clase FastAPI y se asigna a la variable app. Esta instancia se utilizará para definir los endpoints de la API y manejar las solicitudes HTTP.

@app.get("/") # El decorador @app.get("/") se utiliza para definir un endpoint que responde a solicitudes GET en la ruta raíz ("/") de la API. Esto significa que cuando un cliente realiza una solicitud GET a la URL base de la API, se ejecutará la función read_root() y se devolverá la respuesta definida en esa función.
def read_root(): # Se define la función read_root() que se ejecutará cuando se realice una solicitud GET a la ruta raíz ("/") de la API. Esta función devuelve un diccionario con un mensaje de saludo, que se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente.
    return {"Hello": "World"} # Se devuelve un diccionario con un mensaje de saludo, que se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente cuando se realice una solicitud GET a la ruta raíz ("/") de la API. En este caso, el diccionario contiene una clave "Hello" con el valor "World", lo que resultará en una respuesta JSON como {"Hello": "World"} cuando se acceda a la ruta raíz de la API.



''' Creacion de API con FastAPI y Pydantic'''

from fastapi import FastAPI # FastAPI es un framework web moderno y rápido para construir APIs con Python. Proporciona una forma sencilla de crear endpoints y manejar solicitudes HTTP, lo que facilita el desarrollo de aplicaciones web y servicios RESTful.
from pydantic import BaseModel # Pydantic es una biblioteca de validación de datos y gestión de modelos en Python. Se utiliza para definir modelos de datos que pueden ser validados automáticamente, lo que facilita la creación de APIs y la gestión de datos en aplicaciones web.

app = FastAPI() # Se crea una instancia de la clase FastAPI y se asigna a la variable app. Esta instancia se utilizará para definir los endpoints de la API y manejar las solicitudes HTTP.

guardar_usuario = [] # Se define una lista vacía llamada guardar_usuario, que se utilizará para almacenar los usuarios creados a través de la API.

class Usuario(BaseModel): # Se define una clase llamada Usuario que hereda de BaseModel de Pydantic. Esta clase se utiliza para definir el modelo de datos de un usuario, con atributos como nombre, edad, correo y teléfono. Al heredar de BaseModel, se habilita la validación automática de los datos cuando se reciben solicitudes a través de la API.
    nombre: str # Se define un atributo nombre de tipo str (cadena de texto) en la clase Usuario.
    edad: int # Se define un atributo edad de tipo int (entero) en la clase Usuario.
    correo : str # Se define un atributo correo de tipo str (cadena de texto) en la clase Usuario.
    telefono: int # Se define un atributo telefono de tipo int (entero) en la clase Usuario.

class Mensaje(BaseModel): # Se define una clase llamada Mensaje que hereda de BaseModel de Pydantic. Esta clase se utiliza para definir el modelo de datos de un mensaje, con un atributo mensaje de tipo str (cadena de texto). Al heredar de BaseModel, se habilita la validación automática de los datos cuando se reciben solicitudes a través de la API.
    mensaje: str # Se define un atributo mensaje de tipo str (cadena de texto) en la clase Mensaje.

# Endpoint para recibir un mensaje
@app.post("/mensaje") # El decorador @app.post("/mensaje") se utiliza para definir un endpoint que responde a solicitudes POST en la ruta "/mensaje" de la API. Esto significa que cuando un cliente realiza una solicitud POST a la URL base de la API seguida de "/mensaje", se ejecutará la función recibir_mensaje() y se procesará el mensaje enviado en la solicitud.
def recibir_mensaje(mensaje: Mensaje): # Se define la función recibir_mensaje()
    return { # Se devuelve un diccionario con la clave "mensaje recibido" y el valor del atributo mensaje del objeto Mensaje recibido en la solicitud. Este diccionario se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente cuando se realice una solicitud POST a la ruta "/mensaje" de la API.
    "mensaje recibido" : mensaje.mensaje
    }

# Crear un nuevo usuario
@app.post("/usuarios") # El decorador @app.post("/usuarios") se utiliza para definir
    #un endpoint que responde a solicitudes POST en la ruta "/usuarios" de la API. Esto significa que cuando un cliente realiza una solicitud POST a la URL base de la API seguida de "/usuarios", se ejecutará la función crear_usuario() y se procesará el usuario enviado en la solicitud para crear un nuevo usuario.
def crear_usuario(usuario: Usuario): # Se define la función crear_usuario() que toma un parámetro usuario de tipo Usuario (definido anteriormente como un modelo de datos con Pydantic). Esta función se ejecutará cuando se realice una solicitud POST a la ruta "/usuarios" de la API, y el objeto usuario se llenará automáticamente con los datos enviados en la solicitud, validando su formato según lo definido en el modelo Usuario.
    guardar_usuario.append(usuario) # Se agrega el objeto usuario a la lista guardar_usuario, lo que permite almacenar los usuarios creados a través de la API en memoria.

    return { # Se devuelve un diccionario con un mensaje de éxito y el usuario creado. Este diccionario se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente cuando se realice una solicitud POST a la ruta "/usuarios" de la API.
        "mensaje": "Usuario creado exitosamente",
            "usuario": usuario
            }

# Listar todos los usuarios
@app.get("/usuarios") # El decorador @app.get("/usuarios") se utiliza para definir
    #un endpoint que responde a solicitudes GET en la ruta "/usuarios" de la API. Esto significa que cuando un cliente realiza una solicitud GET a la URL base de la API seguida de "/usuarios", se ejecutará la función lista_usuarios() y se devolverá la lista de usuarios almacenados en guardar_usuario como respuesta al cliente.
def lista_usuarios(): # Se define la función lista_usuarios() que se ejecutará cuando
    #se realice una solicitud GET a la ruta "/usuarios" de la API. Esta función devuelve la lista guardar_usuario, que contiene los usuarios creados a través de la API, y se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente.
    return guardar_usuario

@app.get("/usuario/{nombre}") # El decorador @app.get("/usuario/{nombre}") se utiliza para definir un endpoint que responde a solicitudes GET en la ruta "/usuario/{nombre}" de la API, donde {nombre} es un parámetro de ruta que representa el nombre del usuario que se desea buscar. Esto significa que cuando un cliente realiza una solicitud GET a la URL base de la API seguida de "/usuario/" y el nombre del usuario, se ejecutará la función buscar_usuario() y se procesará el nombre enviado en la solicitud para buscar un usuario específico en la lista guardar_usuario.
def buscar_usuario(nombre: str): # Se define la función buscar_usuario() que toma un pará
#metro nombre de tipo str (cadena de texto). Esta función se ejecutará cuando se realice una solicitud GET a la ruta "/usuario/{nombre}" de la API, y el valor del parámetro nombre se llenará automáticamente con el nombre enviado en la solicitud.

    for usuario in guardar_usuario: # Se itera sobre cada usuario almacenado en la lista guardar_usuario para buscar un usuario que coincida con el nombre proporcionado en la solicitud.

     if usuario.nombre.lower() == nombre.lower(): # Se compara el atributo nombre de cada usuario con el valor del parámetro nombre, convirtiendo ambos a minúsculas para hacer la comparación insensible a mayúsculas. Si se encuentra una coincidencia, se devuelve el usuario encontrado como respuesta al cliente.
        return usuario
    
    return {"mensaje": "Usuario no encontrado"} # Si no se encuentra ningún usuario que coincida con el nombre proporcionado, se devuelve un diccionario con un mensaje indicando que el usuario no fue encontrado. Este diccionario se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente.


#eliminar un usuario
@app.delete("/usuario/{nombre}") # El decorador @app.delete("/usuario/{nombre}")
def eliminar_usuario(nombre: str): # Se define la función eliminar_usuario() que toma un parámetro nombre de tipo str (cadena de texto). Esta función se ejecutará cuando se realice una solicitud DELETE a la ruta "/usuario/{nombre}" de la API, y el valor del parámetro nombre se llenará automáticamente con el nombre enviado en la solicitud.

    for usuario in guardar_usuario: # Se itera sobre cada usuario almacenado en la lista guardar_usuario para buscar un usuario que coincida con el nombre proporcionado en la solicitud.

     if usuario.nombre.lower() == nombre.lower(): # Se compara el atributo nombre de cada usuario con el valor del parámetro nombre, convirtiendo ambos a minúsculas para hacer la comparación insensible a mayúsculas. Si se encuentra una coincidencia, se elimina el usuario encontrado de la lista guardar_usuario y se devuelve un mensaje indicando que el usuario fue eliminado exitosamente.
        guardar_usuario.remove(usuario) # Se elimina el usuario encontrado de la lista guardar_usuario utilizando el método remove().
        return {"mensaje": "Usuario eliminado exitosamente"} # Se devuelve un diccionario con un mensaje indicando que el usuario fue eliminado exitosamente. Este diccionario se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente.

    return {"mensaje": "Usuario no encontrado"} # Si no se encuentra ningún usuario que coincida con el nombre proporcionado, se devuelve un diccionario con un mensaje indicando que el usuario no fue encontrado. Este diccionario se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente.


#Actualizar un usuario
@app.put("/usuario/{nombre}") # El decorador @app.put("/usuario/{nombre}")

def actualizar_usuario(nombre: str, usuario_actualizado: Usuario): # Se define la función actualizar_usuario() que toma dos parámetros: nombre de tipo str (cadena de texto) y usuario_actualizado de tipo Usuario (definido anteriormente como un modelo de datos con Pydantic). Esta función se ejecutará cuando se realice una solicitud PUT a la ruta "/usuario/{nombre}" de la API, y el valor del parámetro nombre se llenará automáticamente con el nombre enviado en la solicitud, mientras que el objeto usuario_actualizado se llenará con los datos enviados en el cuerpo de la solicitud para actualizar un usuario específico.
    for usuario in guardar_usuario: # Se itera sobre cada usuario almacenado en la lista guardar_usuario para buscar un usuario que coincida con el nombre proporcionado en la solicitud.

     if usuario.nombre.lower() == nombre.lower(): # Se compara el atributo nombre de cada usuario con el valor del parámetro nombre, convirtiendo ambos a minúsculas para hacer la comparación insensible a mayúsculas. Si se encuentra una coincidencia, se actualizan los atributos del usuario encontrado con los valores del objeto usuario_actualizado y se devuelve un mensaje indicando que el usuario fue actualizado exitosamente.
        usuario.nombre = usuario_actualizado.nombre # Se actualiza el atributo nombre del usuario encontrado con el valor del atributo nombre del objeto usuario_actualizado.
        usuario.edad = usuario_actualizado.edad # Se actualiza el atributo edad del usuario encontrado con el valor del atributo edad del objeto usuario_actualizado.
        usuario.correo = usuario_actualizado.correo # Se actualiza el atributo correo del usuario encontrado con el valor del atributo correo del objeto usuario_actualizado.
        return {"mensaje": "Usuario actualizado exitosamente"} # Se devuelve un diccionario con un mensaje indicando que el usuario fue actualizado exitosamente. Este diccionario se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente.

    return {"mensaje": "Usuario no encontrado"} # Si no se encuentra ningún usuario que coincida con el nombre proporcionado, se devuelve un diccionario con un mensaje indicando que el usuario no fue encontrado. Este diccionario se convertirá automáticamente en formato JSON para ser enviado como respuesta al cliente.







