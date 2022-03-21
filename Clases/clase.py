# ejercicio: comprobar si una cadena de caracteres es palíndromo

class Palindromo():
    def esPalindromo(arg):
        arg = input("Introduzca la palabra que desee saber si es un palíndromo. " )
        
        if str(arg) == "".join(reversed(arg)):
            print("Es un palíndromo")
        else:
            print("No es palíndromo")
        
        longitud = len(arg)
        if longitud < 1:
            print(True)
        else:
            if arg[0] == arg[-1]:
                Palindromo.esPalindromo(arg[1:-1])
            else:
                print("El argumento introducido no es un palíndromo. ")
        