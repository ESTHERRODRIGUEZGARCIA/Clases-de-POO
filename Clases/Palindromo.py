# ejercicio: comprobar si una cadena de caracteres es palíndromo

class Palindromo():
    def esPalindromo(arg):
        arg = input()
        arg = arg.lower() #texto en minúsculas
        arg = arg.replace(" ", "") # elimina espacios
        n, m = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN' 
        tilde = str.maketrans(n, m)
        arg = arg.translate(tilde) #elimina tildes
        if str(arg) == "".join(reversed(arg)):
            print(True)
            print(arg, " sí es un palíndromo. ")
        else:
            print(False)
            print(arg, " no es un palíndromo. ")
        
        