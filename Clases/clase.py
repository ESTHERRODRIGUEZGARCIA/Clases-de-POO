# ejercicio: comprobar si una cadena de caracteres es palíndromo

class Palindromo():
    word = input()
    if str(word) == str(word)[::-1] :
        print("Palíndromo")
    else:
        print("Not Palíndromo")