#Operaciones simples
print(10 + 5)
print(22 - 10)
print(10 * 3)
print(24 / 2)

#Concatenaciones
print(1, 2, 3)
print("Hoy es día", 30, "de abril")
print("Hola" * 5)

#Operaciones declarando variables
a = 2
b = 4
c = 5
print(a + b)
print((a + c) * 5)
print(c - b)
print(a + 3.5)

#Calcular la raíz cuadrada de un número
print("- Vamos a calcular la raíz cuadrada de un número")
import math
num = int(input("Introduce un número entero: "))
raiz = math.sqrt(num)
print("La raíz cuadrada de", num, "es", raiz)

#Calcular el área de un rectángulo
print("- Vamos a calcular el área de un rectángulo")
base = float(input("Introduce la base en cm: "))
altura = float(input("Introduce la altura en cm: "))
area = base * altura
print("El área del rectángulo es", area)

#Calcular el perímetro de una circunferencia
print("- Vamos a calcular el perímetro de una circunferencia")
PI = 3.14
radio = float(input("Introduce el radio en cm: "))
perimetro = (2 * PI) * radio
print("El perímetro de la circunferencia es", perimetro)

#Calcular el índice de Masa Corporal de una persona
print("- Calcula tu índice de Masa Corporal")
persona = input("Introduce un nombre: ")
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en m: "))
IMC = peso / (altura ** 2)
print("El IMC de", persona, "es de", IMC)

#Convertir de grados Celsius a Fahrenheit
print("- Convierte grados Celsius en grados Fahrenheit")
celsius = int(input("Introduce los grados Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(celsius, "ºC", "equivalen a", fahrenheit, "ºF")