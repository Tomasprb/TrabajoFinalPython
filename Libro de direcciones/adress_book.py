import os
import random
from datetime import datetime
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'adresses.csv')

archivo=open(filename, "a")
archivo.write("id,nombre,direccion,telefono,fecha")
archivo.close()
nombre=""
direccion=""
telefono=""


def Ingreso(nom,dir,tel):
    output="\n"
    output+=str(random.randint(0 , 65536))+","
    output+=nom+","
    output+=dir+","
    output+=tel+","
    output+=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    archivo=open(filename, "a")
    archivo.write(output)
    archivo.close()
    print("entrada creada con exito")
while True:
    nombre=input("ingrese un nombre: ")
    if nombre=="exit":
        break
    direccion=input("ingrese una direccion: ")
    telefono=input("ingrese un telefono: ")
    Ingreso(nombre,direccion,telefono)