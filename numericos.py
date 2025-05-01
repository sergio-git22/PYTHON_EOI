#Encontrar el área de un rectángulo dado su ancho y alto.
print("- Calcula el área de un rectángulo")
ancho = float(input("Introduce el ancho en cm: "))
alto = float(input("Introduce el alto en cm: "))
area = ancho * alto
print("El área del rectángulo es", area)

#Calcular el perímetro de un círculo dado su radio. (import math)
print("- Calcula el perímetro dado su radio")
import math
radio = 5
perimetro = 2 * math.pi * radio
print("El perímetro del círculo es", perimetro)

#Convertir grados Celsius a Fahrenheit.
print("- ¿A cuántos grados Fahrenheit equivalen los siguientes grados Celsius?")
celsius = int(input("Escribe los grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "ªC equivalen a", fahrenheit, "ªF")

#Calcular la raíz cuadrada de un número
print("- Calcula la raíz cuadrada de un número")
import math
num = 49
raiz = math.sqrt(num)
print("La raíz cuadrada de", num, "es", raiz)

#Determinar si un número es par o impar.
print("- Comprueba si el número introducido es par o impar")
num = int(input("Introduce un número entero: "))
if num % 2 == 0:
    print("El número", num, "es par")
else:
    print("El número", num, "es impar")

#Calcular el área de un círculo dado su radio.
print("- Calcula el área de un círculo dado su radio")
import math
radio = 7
area = math.pi * (radio ** 2)
print("El área del círculo es", area)

#Calcular la suma de los dígitos de un número entero
print("- Suma los dígitos de un número entero")
num = 1234
suma = 0
for digito in str(num):
    suma += int(digito)
print("La suma de los dígitos del número es", suma)

#Calcular el promedio de una lista de números
print("- Vamos a calcular la media de una lista de números")
numeros = [4, 12, 23, 36]
promedio = sum(numeros) / len(numeros)
print("La media de los números es", promedio)

#Ordenar una lista de números de forma ascendente
print("- Ordena una lista de números de forma ascendente")
numeros = [93, 73, 63, 12]
numeros.sort()
print(numeros)