#1
print("- Crear una lista bidimensional que represente una matriz de 3x3 y llenarla con números aleatorios del 1 al 9. Mostrar la matriz resultante.")
import random

matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(random.randint(1, 9))
    matriz.append(fila)

for fila in matriz:
    print(fila)

#2
print("- Dada una matriz de 3x3, calcular la suma de todos sus elementos.")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
suma = 0
for fila in matriz:
    for elem in fila:
        suma += elem

print("La suma de los elementos de la matriz es", suma)

#3
print("- Crear una lista bidimensional que represente una matriz de 4x4 y llenarla con el valor 0. Mostrar la matriz resultante.")
matriz = []
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)

#4
print("- Dada una matriz de 4x4, rellenar la diagonal principal con el valor 1 y mostrar la matriz resultante.")
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(4):
    matriz[i][i] = 1

for fila in matriz:
    print(fila)

#5
print("- Crear una lista bidimensional que represente una matriz de 5x5 y llenarla con números aleatorios del 1 al 100. Mostrar la matriz resultante y encontrar el valor máximo y mínimo de la matriz.")
import random
matriz = []

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(random.randint(1, 100))
    matriz.append(fila)

for fila in matriz:
    print(fila)

maximo = max(max(fila) for fila in matriz)
minimo = min(min(fila) for fila in matriz)

print("El número máximo de la matriz es", maximo)
print("El número mínimo de la matriz es", minimo)

#6
print("- Dada una matriz de 3x3, mostrar la suma de cada fila y de cada columna.")
matriz = [[6, 12, 23], [4, 25, 63], [11, 33, 55]]
for fila in matriz:
    suma_fila = sum(fila)
    print(f"Suma de la fila {matriz.index(fila)+1}: {suma_fila}")

for j in range(len(matriz[0])):
    suma_columna = sum(matriz[i][j] for i in range(len(matriz)))
    print(f"Suma de la columna {j+1}: {suma_columna}")

#7
print("- Crear una lista bidimensional que represente una matriz de 4x4 y llenarla con números aleatorios del 1 al 100. Mostrar la matriz resultante ordenada por filas de forma ascendente.")
import random
matriz = []

for i in range(4):
    fila = []
    for j in range(4):
        fila.append(random.randint(1, 100))
    matriz.append(fila)

for fila in matriz:
    print(sorted(fila))

#8
print("- Dada una matriz de 3x3, mostrar la diagonal secundaria.")
matriz = [[2, 6, 15], [3, 5, 7], [12, 14, 16]]

diagonal_secundaria = [matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz)) if i + j == len(matriz) -1]
print(diagonal_secundaria)

#9
print("- Dada una matriz de 4x4, mostrar la matriz resultante de intercambiar la primera fila con la última.")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print("MATRIZ ORIGINAL")
for fila in matriz:
    print(fila)

matriz [0], matriz[-1] = matriz[-1], matriz[0]

print("MATRIZ RESULTANTE")
for fila in matriz:
    print(fila)