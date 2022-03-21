from Clases.Palindromo import *


def ejercicios():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \n1. Palíndromo - método de clase\n2. Palíndromo - método de instancias\n3. Puzzle \n4. Logger\n"))
    if variable == 1:
        arg = input("¿Qué argumento quieres comprobar? \n")
        Palindromo.esPalindromo(arg)
    elif variable == 2:
        from Clases import instancia
    elif variable == 3:
        from Clases import puzzle

ejercicios()