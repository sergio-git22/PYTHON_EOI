#1
print("- Escribir un programa que imprima los números del 1 al 10.")
for i in range(1, 11):
    print(i)

#2
print("- Escribir un programa que calcule la suma de los primeros 100 números naturales.")
suma = 0
for i in range(1, 101):
    suma += i
print("La suma de los primeros 100 números naturales es", suma)

#3
print("- Escribir un programa que lea una cadena de caracteres y cuente cuántas veces aparece la letra 'a'.")
texto = str(input("Escribe una cadena de texto: "))
contador = 0
for letra in texto:
    if letra == "a":
        contador += 1
print("La letra 'a' aparece", contador, "veces en la cadena de texto")

#4
print("- Escribir un programa que calcule el factorial de un número entero positivo.")
num = int(input("Introduce un número entero: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print("El factorial del", num, "es", factorial)

#5
print("- Escribir un programa que lea una lista de números y calcule su suma.")
numeros = [4, 12, 23, 35]
suma = 0
for i in numeros:
    suma += i
print("La suma de los números", numeros, "es", suma)

#6
print("- Escribir un programa que lea una lista de números y calcule su promedio.")
numeros = [3, 11, 24, 41]
suma = 0
for numero in numeros:
    suma += numero
    promedio = suma / len(numeros)
print("El promedio de los números", numeros, "es", promedio)

#7
print("- Escribir un programa que lea una lista de palabras y muestre la longitud de cada una.")
palabras = ['ordenador', 'desarrollo', 'web']
for palabra in palabras:
    print("La palabra", palabra, "tiene", len(palabra), "letras")

#8
print("- Escribir un programa que imprima los números pares del 1 al 20.")
for i in range(2, 21, 2):
    print(i)

#9
print("- Escribir un programa que lea una lista de números y calcule su máximo.")
numeros = [8, 12, 23, 37]
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print("El número más alto de los números", numeros, "es", maximo)

#9 (sin for)
print("- Escribir un programa que lea una lista de números y calcule su máximo.")
numeros = [8, 12, 23, 37]
print("El número más alto de los números", numeros, "es", max(numeros))

#10
print("- Escribir un programa que lea una lista de números y calcule su mínimo.")
numeros = [8, 12, 23, 37]
minimo = numeros[0]
for numero in numeros:
    if numero < minimo:
        minimo = numero
print("El número más bajo de los números", numeros, "es", minimo)

#10 (sin for)
print("- Escribir un programa que lea una lista de números y calcule su mínimo.")
numeros = [8, 12, 23, 37]
print("El número más bajo de los números", numeros, "es", min(numeros))