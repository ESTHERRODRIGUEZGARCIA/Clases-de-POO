<h1 align="center">Clases de POO</h1>

[Repositorio](https://github.com/ESTHERRODRIGUEZGARCIA/Clases-de-POO.git) con los ejercicios de clases utilizando la Programación Orientada a Objetos.

***

Trabajo realizado por: 
1. Esther Rodríguez
2. Teresa Álvarez

# ÍNDICE 
a. Palíndromo - método de clase

b. Palíndromo - método de instancia

c. Puzzle

d. Logger

***

# Palíndromo - método de clase
Enunciado: 

Crear una clase Palindromo que contenga un método de clase esPalindromo(), que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda. Se tienen en cuenta los caracteres no alfanuméricos.

Pregunta adicional: ¿por qué se muestra RADAR después de la instanciación Palindromo("sonar")?

El código empleado para resolver este ejercicio es el siguiente:

````
# ejercicio: comprobar si una cadena de caracteres es palíndromo

class Palindromo():
    def esPalindromo(arg):
        n, m = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN' 
        tilde = str.maketrans(n, m)
        arg = arg.lower() #texto en minúsculas
        arg = arg.replace(" ", "") # elimina espacios
        arg = arg.translate(tilde) #elimina tildes
        lista=list(arg)
        listareversa=list(reversed(arg))
        if lista == listareversa:
            print("True")
            print(arg, " sí es un palíndromo. ")
        else:
            print(False)
            print(arg, " no es un palíndromo. ")
    arg = str(input("Introduce para ver si es palindromo: "))
    esPalindromo(arg)

````

UML:



# Palíndromo - método de instancia
Enunciado: 

En esta misma clase Palindromo, añada un atributo que se inicializará en el constructor. Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo. Además, al destruir la instancia, muestre el atributo en mayúsculas.

````

class instancia():
    def Palindromos(tema):
        a,b= 'áéíóúÁÉÍÓÚüÜÑñ', 'aeiouAEIOUuUnN'
        tilde = str.maketrans(a,b)
        tema = tema.lower()
        tema = tema.replace(" ", "")
        tema = tema.translate(tilde)
        print(tema.upper())
        lista = list(tema)
        resultadolista= list(reversed(tema))
        if lista == resultadolista:
            print("Es palindromo!")
        else:
            print("No es palindromo!")
    tema= str(input("Introduce una numero, palabra o frase para comprobar si es palindromo: "))
    Palindromos(tema)
    
````

UML:


# Puzzle
Enunciado: 
Adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

````
class A:                    # estructura principal 
    def z(self):            # función
        return self 
 
    def y(self, t):         # función
        return len(t) 
 
a = A                       # vuelve a la clase A
y = a.z                     # sigue formando parte de la clase A por la anterior condición
print(y(a))                 # me devuelve <class 'Clases.puzzle.A'> por el self definido en z
aa = a()                    # instancia
print(aa is a())            # False pues la condición no es verdadera
z = aa.y                    # función
print(z(()))                # tupla vacía, devuelve el valor 0
print(a().y((a,)))          # tupla que devuelve len(a). Es 1 por estar formada sólo por a
print(A.y(aa, (a,z)))       # tupla que devuelve la longitud. Es 2 por estar formada tanto por a como por z
print(aa.y((z,1,'z')))      # tupla que devuelve len( z, 1, 'z') que son 3 elementos


````
output:

````
<class 'Clases.puzzle.A'>
False
0
1
2
3

````

UML:


# Logger
Enunciado: 
Escriba una clase Logger, cuyo objetivo sea escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje). La primera línea del archivo debe ser "--Start log--", seguida de los mensajes recibidos por el método log en la parte superior de un mensaje por línea, y la última línea del archivo, escrita cuando se destruye la instancia de Logger, debe ser "--End log: x log (s) -" donde x es el número de llamadas al método log. Esta clase Logger se utilizará en un método llamada() de una clase Test.

````

import logging

class logger():
    #objetivo: escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje).
    def llamada():
        mensaje= str(input("¿Qué mensaje desea escribir?: "))
        veces = int(input("¿Cuántas veces desea recibir el mensaje?: "))
        archivo = open("logger.txt", "a") #add
        

        archivo.write("---Start log---\n")
        for i in range(veces):
            archivo.write(mensaje)


        archivo.write("\n---End log---"+ str(veces))
        archivo.close()
````
UML:
