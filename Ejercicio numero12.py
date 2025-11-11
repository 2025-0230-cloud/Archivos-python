#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
""""""
muestra=input("Introduce una lista de números separados por comas:")

numeros = [float(x) for x in muestra.split(',')]


media = sum(numeros) / len(numeros)
suma_cuadrados = sum((x - media) ** 2 for x in numeros)
desviacion_tipica = (suma_cuadrados / len(numeros)) ** 0.5

print("La medianaes:", media)
print("La desviacion tipca es:", desviacion_tipica )