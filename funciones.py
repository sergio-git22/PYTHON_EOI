#1
print("- Escribe una función llamada calcular_area_circulo que reciba el radio de un círculo y calcule su área. Utiliza la fórmula A = π * r2, donde π es una constante.")
import math

def calcular_area_circulo():
    area = math.pi * radio**2
    return area

radio = 4
area_circulo = calcular_area_circulo()
print("El área del círculo es", area_circulo)

#2
print("- Escribe una función llamada es_primo que reciba un número entero y determine si es primo o no. Un número primo es aquel que solo es divisible por sí mismo y por 1.")
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Introduce un número entero: "))
if es_primo(numero):
    print("El número es primo")
else:
    print("El número no es primo")

#3
print("- Escribe una función llamada contar_vocales que reciba una cadena de texto y cuente la cantidad de vocales que contiene. Considera tanto vocales en mayúsculas como en minúsculas.")
def contar_vocales():
    vocales = "AEIOUaeiou"
    contador = 0
    for i in texto:
        if i in vocales:
            contador += 1
    return contador

texto = str(input("Escribe una cadena de texto: "))
cantidad_vocales = contar_vocales()
print("La cadena de texto tiene", cantidad_vocales, "vocales")

#4
print("- Escribe una función llamada reverso_cadena que reciba una cadena de texto y devuelva su reverso. Por ejemplo, si se recibe la cadena 'Hola', la función debe retornar 'aloH'.")
def reverso_cadena(texto):
    return texto[::-1]

texto = str(input("Escribe una cadena de texto: "))
reverso = reverso_cadena(texto)
print(reverso)

#5
print("- Escribe una función llamada calcular_promedio que reciba una lista de números y calcule su promedio. La función debe retornar el valor promedio.")
def calcular_promedio():
    promedio = sum(numeros) / len(numeros)
    return promedio

numeros = [2, 4, 11, 27]
promedio = calcular_promedio()
print("El promedio de los números es", promedio)

#6
print("- Escribe una función llamada es_palindromo que reciba una cadena de texto y determine si es un palíndromo. Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha y de derecha a izquierda.")
def es_palindromo():
    texto = texto[::-1]
    return texto

texto = str(input("Escribe una cadena de texto: "))
if texto == texto[::-1]:
    print(texto, "es palíndromo")
else:
    print(texto, "no es palíndromo")

#7
print("- Escribe una función llamada suma_numeros_pares que reciba una lista de números y calcule la suma de todos los números pares presentes en la lista.")
def suma_numeros_pares():
    suma = 0
    for i in numeros:
        if i % 2 == 0:
            suma += i
    return suma

numeros = [5, 16, 19, 24, 33, 52]
suma = suma_numeros_pares()
print("La suma de los números pares de la lista es", suma)

#8
print("- Escribe una función llamada generar_primos que reciba un número entero y genere una lista con todos los números primos menores o iguales a ese número.")
def generar_primos(numero):
    primos = []
    for num in range(2, numero + 1):
        if es_primo(num):
            primos.append(num)
    return primos

numero = 20
primos = generar_primos(numero)
print("Números primos hasta", numero, ": ", primos)

#9
print("- Escribe una función llamada calcular_factorial que reciba un número entero y calcule su factorial. El factorial de un número n se define como el producto de todos los números enteros positivos desde 1 hasta n.")
def calcular_factorial(numero):
    factorial = 1
    if numero < 0:
        return "No se puede calcular el factorial de un negativo"
    elif numero == 0:
        return factorial
    else:
        for i in range(1, numero + 1):
            factorial *= i
    return factorial

numero = 5
print(calcular_factorial(5))

#10
print("- Escribe una función llamada celsius_a_fahrenheit que reciba una temperatura en grados Celsius y la convierta a grados Fahrenheit. Utiliza la fórmula F = C * 9/5 + 32, donde F representa grados Fahrenheit y C representa grados Celsius.")
def celsius_a_fahrenheit():
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celsius = int(input("Introduce los grados Celsius: "))
fahrenheit = celsius_a_fahrenheit()
print(celsius, "ºC equivalen a", fahrenheit, "º Fahrenheit")