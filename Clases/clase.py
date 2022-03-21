# ejercicio: comprobar si una cadena de caracteres es palíndromo

class Palindromo():
    def esPalindromo(arg):
        arg = input( )
        
        if str(arg) == "".join(reversed(arg)):
            print("Palíndromo")
        else:
            print("No es Palíndromo")
        
        longitud = len(arg)
        if longitud < 1:
            print(True)
        else:
            if arg[0] == arg[-1]:
                Palindromo.esPalindromo(arg[1:-1])
            else:
                print("El argumento introducido no es un palíndromo. ")
        