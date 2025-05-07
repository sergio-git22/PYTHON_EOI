#1
print("- Encontrar el área de un rectángulo dado su ancho y alto.")
ancho = 8
alto = 5
area = ancho * alto
print("El área del rectángulo es", area)

#2
print("- Calcular el perímetro de un círculo dado su radio.") #import math
import math
radio = 5
perimetro = 2 * math.pi * radio
print("El perímetro del círculo es", perimetro)

#3
print("- Convertir grados Celsius a Fahrenheit.")
celsius = int(input("Escribe los grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "ªC equivalen a", fahrenheit, "ªF")

#4
print("- Calcular la raíz cuadrada de un número.")
import math
num = 49
raiz = math.sqrt(num)
print("La raíz cuadrada de", num, "es", raiz)

#5
print("- Determinar si un número es par o impar.")
num = int(input("Introduce un número entero: "))
if num % 2 == 0:
    print("El número", num, "es par")
else:
    print("El número", num, "es impar")

#6
print("- Calcular el área de un círculo dado su radio.")
import math
radio = 7
area = math.pi * (radio ** 2)
print("El área del círculo es", area)

#7
print("- Calcular la suma de los dígitos de un número entero.")
num = 1234
suma = 0
for digito in str(num):
    suma += int(digito)
print("La suma de los dígitos del número es", suma)

#8
print("- Calcular el promedio de una lista de números.")
numeros = [4, 12, 23, 36]
promedio = sum(numeros) / len(numeros)
print("La media de los números es", promedio)

#9
print("- Ordenar una lista de números de forma ascendente.")
numeros = [93, 73, 63, 12]
numeros.sort()
print(numeros)