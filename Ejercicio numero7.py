#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
""""""
Abecedario=list("abcdefghijklmnopqrstuvwxyz")

Nueva_lista = [letra for i, letra in enumerate(Abecedario) 
               
if (i + 1) % 3 != 0]

print("Lista original:", Abecedario)
print("Lista sin las letras en posiciones múltiplos de 3:", Nueva_lista)






