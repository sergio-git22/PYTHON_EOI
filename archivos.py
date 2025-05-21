#1
print("- Leer un archivo de texto y mostrar su contenido por pantalla.")
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#2
print("- Leer un archivo de texto y mostrar las líneas que contienen una palabra en particular.")
with open("archivo.txt", "r") as archivo:
    palabra = "texto"
    for linea in archivo:
        if palabra in linea:
            print(linea)

#3
print("- Escribir una lista de números en un archivo de texto.")
numeros = [1, 2, 3, 4, 5]

with open("numeros.txt", "w") as archivo:
    for numero in numeros:
        archivo.write(str(numero) + "\n")

#4
print("- Leer un archivo de texto que contiene números separados por comas y mostrar la suma de los números.")
with open("numeros.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    numeros = contenido.split(",")
    suma = sum(map(int, numeros))
    print(suma)

#5
print("- Escribir una lista de palabras en un archivo de texto, separadas por espacios.")
palabras = ["Hoy", "es", "miercoles"]

with open("palabras.txt", "w") as archivo:
    archivo.write(" ".join(palabras))

#6
print("- Leer un archivo de texto que contiene una lista de palabras separadas por espacios y mostrar la cantidad de palabras que comienzan con una letra determinada.")
with open("palabras.txt", "r") as archivo:
    contenido = archivo.read()
    palabras = contenido.split()
    letra = "m"
    cantidad = sum(1 for palabra in palabras if palabra.startswith(letra))
    print("Hay", cantidad, "palabras que empieza por M")

#7
print("- Escribir una lista de tuplas en un archivo CSV. (investiga csv.writer)")
import csv

datos = [("Marc", "Marquez", 93), ("Jorge", "Lorenzo", 99), ("Dani", "Pedrosa", 26)]

with open("datos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    for fila in datos:
        escritor.writerow(fila)

#8
print("- Leer un archivo CSV que contiene una lista de tuplas y mostrar el nombre de la persona más joven. (csv.reader)")
import csv

with open("datos.csv", "r", newline="") as archivo:
    lector = csv.reader(archivo)
    numeros = []
    for fila in lector:
        numeros.append(int(fila[2]))
    numero_minimo = min(numeros)
    archivo.seek(0)
    for fila in lector:
        if int(fila[2]) == numero_minimo:
            print(fila[0])