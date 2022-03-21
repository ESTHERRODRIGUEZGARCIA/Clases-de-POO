# ejercicio: comprobar si una cadena de caracteres es palíndromo

class Palindromo():
    def esPalindromo(arg):
        arg = input( )
        
        if str(arg) == str(arg)[::-1] :
            print("Palíndromo")
        else:
            print("No es Palíndromo")
        
        longitud = len(arg)
        if longitud % 2 == 0:
            Palindromo.esPalindromo(arg[1:-1])
        else:
            print("El argumento introducido no es un palíndromo. ")