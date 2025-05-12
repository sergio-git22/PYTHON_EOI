#1
print("- Escribir un programa que imprima los números pares del 2 al 10 utilizando un bucle while.")
numero = 2
while numero <= 10:
    print(numero)
    numero += 2

#2
print("- Escribir un programa que solicite al usuario un número y que muestre la tabla de multiplicar correspondiente a ese número utilizando un bucle while.")
numero = int(input("Introduce un número entero: "))
i = 1
while i <= 10:
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
    i += 1

#3
print("- Escribir un programa que calcule la suma de los números del 1 al 100 utilizando un bucle while.")
numero = 1
suma = 0
while numero <= 100:
    suma += numero
    numero += 1
print("La suma es: ", suma)

#4
print("- Escribir un programa que solicite al usuario un número y que calcule el factorial de ese número utilizando un bucle while.")
numero = int(input("Introduce un número entero: "))
factorial = 1
while numero > 0:
    factorial *= numero
    numero -= 1
print("El factorial es: ", factorial)

#5
print("- Escribir un programa que solicite al usuario una palabra y que imprima la palabra al revés utilizando un bucle while.")
palabra = str(input("Escribe una palabra: "))
while palabra:
    print(palabra[::-1])
    break

#6
print("- Escribir un programa que solicite al usuario un número y que imprima todos los números impares desde ese número hasta 1 utilizando un bucle while.")
numero = int(input("Introduce un número entero: "))
while numero >= 1:
    if numero % 2 != 0:
        print(numero)
    numero -= 1

#7
print("- Escribir un programa que solicite al usuario un número y que determine si ese número es primo o no utilizando un bucle while.")
numero = int(input("Introduce un número entero: "))
es_primo = True
i = 2
while i < numero:
    if numero % i == 0:
        es_primo = False
        break
    i += 1
if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")

#8
print("- Escribir un programa que solicite al usuario una frase y que cuente cuántas vocales hay en la frase utilizando un bucle while.")
vocales = "AEIOUaeiouÁÉÍÓÚáéíóú"
contador = 0
i = 0
frase = str(input("Escribe una frase: "))
while i < len(frase):
    if frase[i] in vocales:
        contador += 1
    i += 1
print("La frase tiene", contador, "vocales")