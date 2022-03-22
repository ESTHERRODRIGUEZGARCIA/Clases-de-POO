class instantcia():
    def palindromo():
        a,b= 'áéíóúÁÉÍÓÚüÜÑñ', 'aeiouAEIOUnN'
        tilde = str.maketrans(a,b)
        tema = tema.lower()
        tema = tema.replace(" ", "")
        lista = list(tema)
        resultado = list(reversed(tema))

        if lista == resultado:
            print("Es palindromo!")
        else:
            print("No es palindromo!")


    tema= str(input())