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

# Palíndromo - método de instancia
Enunciado: 

En esta misma clase Palindromo, añada un atributo que se inicializará en el constructor. Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo. Además, al destruir la instancia, muestre el atributo en mayúsculas.

# Puzzle
Enunciado: 
Adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

````

class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z'))) 

````

# Logger
Enunciado: 
Escriba una clase Logger, cuyo objetivo sea escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje). La primera línea del archivo debe ser "--Start log--", seguida de los mensajes recibidos por el método log en la parte superior de un mensaje por línea, y la última línea del archivo, escrita cuando se destruye la instancia de Logger, debe ser "--End log: x log (s) -" donde x es el número de llamadas al método log. Esta clase Logger se utilizará en un método llamada() de una clase Test.

