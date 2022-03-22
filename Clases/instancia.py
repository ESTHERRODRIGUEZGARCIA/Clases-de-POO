
def palindromos(tema):
    a,b= 'áéíóúÁÉÍÓÚüÜÑñ', 'aeiouAEIOUuUnN'
    tilde = str.maketrans(a,b)
    tema = tema.lower()
    tema = tema.replace(" ", "")
    tema = tema.translate(tilde)
    print(tema.upper())
    lista = list(tema)
    resultadolista= list(reversed(tema))
    if lista == resultadolista:
        print("Es palindromo!")
    else:
        print("No es palindromo!")
tema= str(input("Introduce una numero, palabra o frase para comprobar si es palindromo: "))
palindromos(tema)