
import logging

class logger():
    #objetivo: escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje).
    def llamada(metodo):
        mensaje= str(input("¿Qué mensaje desea escribir?: "))
        veces = str(input("¿Cuántas veces desea recibir el mensaje?: "))
        archivo = open("logger.txt", "a") #add
        

        print("---Start log---")
        for i in range(veces):
            archivo.write(mensaje)

        print("---End log---")

    
