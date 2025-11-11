#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
""""""

palabra=input("ingrese una palabra:")

palabra = palabra.lower()

if palabra == palabra[::-1]:
    print(" La palabra es un palindrimo.")

else:
    print("La palabra no es un palindrimo.")