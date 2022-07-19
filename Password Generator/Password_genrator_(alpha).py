def contraseña(datos):
    if(datos=='mayuscula ' or datos =='minucula' or datos =='numeros' or datos =='caracteres especiales'):
       return("contraseña aleatoria")
    else:
        return("contraseña 16 digitos alfanumericos")
print("Funcion format")
numero_obtenido= float(input("Ingrese otro numero:"))
print(numero_obtenido)
numero_con_formato =format(numero_obtenido,".2f")
print(numero_con_formato)
