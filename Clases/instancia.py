class instancia:
    def palindromo(tema):
            a,b= 'áéíóúÁÉÍÓÚüÜÑñ', 'aeiouAEIOUnN'
            tilde = str.maketrans(a,b)
            tema = tema.lower()
            tema = tema.replace(" ", "")
            tema = tema.translate(tilde)
            lista = list(tema)
            resultado = list(reversed(tema))

            if lista == resultado:
                print("Es palindromo!")
            else:
                print("No es palindromo!")

            print(tema.upper())
    tema= str(input("Introduce un numero, palabra o frase para comprobar si es palindromo:  "))
    palindromo(tema)