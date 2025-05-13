#1
print("- Escribe un programa que pida al usuario introducir números enteros y los almacene en una lista hasta que el usuario introduzca un número negativo. Luego, imprime la lista.")
numeros = []
while True:
    num = int(input("Introduce un número entero: "))
    if num < 0:
        break
    numeros.append(num)
print(numeros)

#2
print("- Escribe un programa que cree una lista con los números del 1 al 10 y luego los imprima en orden inverso.")
numeros = [1,2,3,4,5,6,7,8,9,10]
#numeros = list(range(1, 11))
numeros.reverse()
print(numeros)

#3
print("- Escribe un programa que cree una lista vacía y luego pida al usuario introducir nombres hasta que el usuario introduzca 'fin'. Luego, ordena la lista alfabéticamente e imprímela.")
nombres = []
while True:
    nombre = str(input("Escribe un nombre o 'fin' para terminar: "))
    if 'fin' in nombre:
        break
    nombres.append(nombre)
nombres.sort()
print(nombres)

#4
print("- Escribe un programa que cree una lista con los números del 1 al 5 y luego inserte el número 0 al principio de la lista. Luego, imprime la lista.")
numeros = list(range(1,6))
numeros.insert(0, 0)
print(numeros)

#5
print("- Escribe un programa que cree una lista con los números del 1 al 10 y luego elimine los números pares de la lista. Luego, imprime la lista.")
numeros = list(range(1, 11))
numeros = [num for num in numeros if num % 2 != 0]
print(numeros)

#6
print("- Escribe un programa que cree dos listas con números enteros y luego las combine en una sola lista ordenada. Luego, imprime la lista.")
lista1 = [4, 10, 6]
lista2 = [23, 11, 8]
#lista_combinada = sorted(lista1 + lista2)
#print(lista_combinada)
lista1.extend(lista2)
lista1.sort()
print(lista1)

#7
print("- Escribe un programa que cree una lista con los nombres de los días de la semana y luego elimine los tres primeros elementos de la lista. Luego, imprime la lista.")
dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
del dias[0:3]
print(dias)

#8
print("- Escribe un programa que cree una lista con los números del 1 al 10 y luego multiplique cada número por 2. Luego, imprime la lista resultante.")
numeros = list(range(1, 11))
numeros = [num * 2 for num in numeros]
print(numeros)

#9
print("- Escribe un programa que cree una lista con los nombres de los planetas del sistema solar y luego elimine los dos últimos elementos de la lista. Luego, imprime la lista resultante.")
planetas = ['mercurio', 'venus', 'marte', 'tierra', 'saturno', 'júpiter', 'urano', 'neptuno']
planetas = planetas[:-2]
print(planetas)
