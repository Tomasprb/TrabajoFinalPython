import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'phrases.txt')
archivo=open(filename,"w")
frase=(input("Ingrese una frase: "))
archivo.writelines([frase, " "])
archivo.close()
palabra= len (frase.split())
cuenta_frases=0
cuenta_palabras=0
cuenta_palabras_frases=0


def MostrarResumen(int1,int2,int3):
    print ("Frases ingresadas:  ", int1 )
    print ("Palabras ingresadas:    ", int2)
    print ("Palabras ingresadas en total hta. ahora:   ", int3 )

while frase!="coco" and frase!= "The End":
    cuenta_frases= cuenta_frases+1
    cuenta_palabras= len (frase.split())
    cuenta_palabras_frases=(cuenta_palabras_frases+cuenta_palabras )
    
    MostrarResumen(cuenta_frases,cuenta_palabras,cuenta_palabras_frases)
    
    frase=(input("Ingrese una frase: "))
    archivo=open(filename,"a")
    archivo.writelines([frase," "])
    archivo.close()

    
else:
    print ("Salió del ciclo")
    archivo.close()
    



   

 
 


    

    
    
  




  
  

  


