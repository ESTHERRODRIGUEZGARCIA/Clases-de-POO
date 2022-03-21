# ejercicio: comprobar si una cadena de caracteres es palíndromo

class Palindromo():
    def esPalindromo(arg):
        arg = input( )
        arg = arg.lower()
        arg = arg.replace(" ", "")
        if str(arg) == "".join(reversed(arg)):
            print(True)
        else:
            print(False)
        
        longitud = len(arg)
        if longitud < 1:
            print(True)
        else:
            if arg[0] == arg[-1]:
                Palindromo.esPalindromo(arg[::-1])
                print("Es un palíndromo. ")
            else:
                print("El argumento introducido no es un palíndromo. ")
        