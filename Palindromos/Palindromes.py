def palindrome(string):
    return string == string[::-1]

PalindromeCounter=0
NormalCounter=0
WordCounter=0

palabra=input("Ingrese una palabra: ")

while palabra != 'aloha' and palabra != 'bye':
    WordCounter+=1
    if palindrome(palabra)==True:
        PalindromeCounter+=1
    else:
        NormalCounter+=1
    palabra=input("Ingrese una palabra: ")
print("la cantidad de palabras fue: ", WordCounter)
print("la cantidad de palindromos fue: ", PalindromeCounter)
print("la cantidad de palabras normales fue: ", NormalCounter)
