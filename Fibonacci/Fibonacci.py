# - La suseción de Fibonacci empieza con 1, 1 (ver link de referencia: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci)
# - Se debe controlar que el numero ingresado sea mayor que 0 (cero)

def Fibonacci(Numero):
    if(Numero==0):
        return 0
    elif(Numero==1):
        return 1
    else:
        return (Fibonacci(Numero-2)+Fibonacci(Numero-1))

n=int(input("Escribir el valor de 'n': "))

print("Secuencia de Fibonacci:")

# La numeración deberia comenzar en 1
for n in range(0, n):
  print(Fibonacci(n))
