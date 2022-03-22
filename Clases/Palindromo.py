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