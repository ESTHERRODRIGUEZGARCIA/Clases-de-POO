# ejercicio: comprobar si una cadena de caracteres es palíndromo

class Palindromo():
    def esPalindromo(arg):
        arg = input( )
        arg = arg.lower() #texto en minúsculas
        arg = arg.replace(" ", "") # elimina espacios
        n, m = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN' 
        tilde = str.maketrans(n, m)
        arg = arg.translate(tilde)
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
        