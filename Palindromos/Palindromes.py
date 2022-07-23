# - Se debe tener en cuenta que el usuario ingresa palabras no frases, por lo cual no seria necesario eliminar los espacios
def palindrome(string):
    string = string.lower().replace(' ', '')
    reversed_string = ''.join(reversed(string))
    return string == reversed_string

PalindromeCounter=0
NormalCounter=0
WordCounter=0

palabra=input("Ingrese una palabra: ")

# suma varias veces una palabra con la variable 'WordCounter'
# En esta linea ...
while palabra != 'aloha' and palabra != 'bye':
    WordCounter+=1
    # ... y en esta linea
    if palindrome(palabra)==True:
        PalindromeCounter+=1
    else:
        NormalCounter+=1
    palabra=input("Ingrese una palabra: ")
    # ... y en esta linea
print("la cantidad de palabras fue: ", WordCounter)
print("la cantidad de palindromos fue: ", PalindromeCounter)
print("la cantidad de palabras normales fue: ", NormalCounter)
