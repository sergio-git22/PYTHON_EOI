#1
print("- Escribir un programa que lea un número entero y determine si es positivo, negativo o cero.")
num = int(input("Introduce un número entero: "))
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")

#2
print("- Escribir un programa que lea dos números enteros y determine cuál es el mayor.")
num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce un número entero: "))
if num1 > num2:
    print("El primer número es mayor")
elif num1 < num2:
    print("El segundo número es mayor")
else:
    print("Los números son iguales")

#3
print("- Escribir un programa que lea un número entero y determine si es par o impar.")
num = int(input("Introduce un número entero: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#4
print("- Escribir un programa que lea tres números enteros y determine cuál es el menor.")
num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce un número entero: "))
num3 = int(input("Introduce un número entero: "))
if num1 < num2 and num1 < num3:
    print("El primer número es el menor")
elif num2 < num1 and num1 < num3:
    print("El segundo número es el menor")
else:
    print("El tercer número es el menor")

#5
print("- Escribir un programa que lea un número entero y determine si es primo o no.")
num = int(input("Introduce un número entero: "))
if num < 2:
    print("El número no es primo")
else:
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")

#6
print("- Escribir un programa que lea dos números enteros y determine si su suma es par o impar.")
num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce un número entero: "))
suma = num1 + num2
if suma % 2 == 0:
    print("La suma", suma,"es par")
else:
    print("La suma", suma,"es impar")

#7
print("- Escribir un programa que lea una cadena de texto y determine si tiene una longitud menor o igual a 10 caracteres.")
texto = str(input("Escribe una cadena de texto: "))
if len(texto) <= 10:
    print("La cadena tiene 10 o menos caracteres")
else:
    print("La cadena tiene más de 10 caracteres")