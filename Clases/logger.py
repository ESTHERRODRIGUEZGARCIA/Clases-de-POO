
import logging

class logger():
    #objetivo: escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje).
    def llamada(metodo):
        mensaje= str(input("¿Qué mensaje desea escribir?: "))
        veces = str(input("¿Cuántas veces desea recibir el mensaje?: "))
        archivo = open("logger.txt", "a") #add
        archivo.write(mensaje)

        print("---Start log---")

        print("---End log---")

        logging.warning('Watch out!')  # will print a message to the console
        logging.info('I told you so')  # will not print anything
