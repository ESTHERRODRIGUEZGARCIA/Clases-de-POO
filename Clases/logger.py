
import logging

class logger():
    #objetivo: escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje).
    def llamada():
        mensaje= str(input("¿Qué mensaje desea escribir?: "))
        veces = int(input("¿Cuántas veces desea recibir el mensaje?: "))
        archivo = open("logger.txt", "a") #add
        

        archivo.write("---Start log---\n")
        for i in range(veces):
            archivo.write(mensaje)


        archivo.write("\n---End log---"+ str(veces), "veces")
        archivo.close()

    
