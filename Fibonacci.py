def Fibonacci(Numero):
    if(Numero==0):
        return 0
    elif(Numero==1):
        return 1
    else:
        return (Fibonacci(Numero-2)+Fibonacci(Numero-1)) 
n=int(input("Escribir el vaor de 'n': "))
print("Secuencia de Fibonacci:")
for n in range(0, n):
  print(Fibonacci(n))
