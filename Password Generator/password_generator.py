import random
leng = input("Ingrese longitud: ")
if leng=='':
    leng=16
up = input("Desea mayusculas? (y/n): ")
if up=='':
    up='y'
low = input("Desea minusculas? (y/n): ")
if low=='':
    low='y'
num = input("Desea numeros? (y/n): ")
if num=='':
    num='y'
sim = input("Desea caracteres especiales? (y/n): ")
if sim=='':
    sim='n'

upList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowList = upList.lower()
numList = "0123456789"
simList = "+-%$&#"

def CarAleatorio(str):
    return str[random.randint(0 , len(str)-1)]
Password=""
charSet=""
if up=='y':
    charSet+=upList
if low=='y':
    charSet+=lowList
if num=='y':
    charSet+=numList
if sim=='y':
    charSet+=simList
for i in range (int(leng)):
    Password+=CarAleatorio(charSet)
print("Su contraseña es: " + Password)