from Clases import Palindromo
from Clases.Palindromo import *
from Clases import Logger
from Clases.Logger import *

def ejercicios():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \na. Palíndromo - método de clase\nb. Palíndromo - método de instancias\nc. Puzzle \nd. Logger\n"))
    if variable == 1:
        arg = input("¿Qué argumento quieres comprobar? \n")
        Palindromo.esPalindromo(arg)