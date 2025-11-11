#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
""""""

numeros = []
for i in range(6):
    numero = int(input("Introduce un número ganador de la lotería primitiva: "))
    numeros.append(numero)

numeros.sort()
print("Números ganadores ordenados de menor a mayor:", numeros)
