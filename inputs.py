print("- Escribir un programa que lea un número entero y determine si está entre 10 y 20 o entre 30 y 40.")
num = int(input("Introduce un número entero: "))
if (num >= 10 and num <= 20) or (num >= 30 and num <= 40):
    print("Sí, el número se encuentra en el rango")
else:
    print("No, el número está fuera de rango")

print("- Escribir un programa que lea dos números enteros y determine si al menos uno de ellos es par.")
num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce un número entero: "))
if num1 % 2 == 0 or num2 % 2 == 0:
    print("Sí, al menos uno de ellos es par")
else:
    print("No, ninguno de ellos es par")

print("- Escribir un programa que lea una cadena de texto y determine si contiene la letra 'a' o la letra 'b'.")
texto = str(input("Escribe una cadena de texto: "))
if 'a' in texto or 'b' in texto:
    print("Sí, la 'a' o la 'b' están en el texto")
else:
    print("No, ninguna de las letras está en el texto")

print("- Escribir un programa que lea dos números enteros y determine si ambos son pares o ambos son impares.")
num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce un número entero: "))
if (num1 % 2 == 0 and num2 % 2 == 0) or (num1 % 2 != 0 and num2 % 2 != 0):
    print("Ambos números son pares o impares")
else:
    print("Los dos números son distintos")

print("- Escribir un programa que lea una cadena de texto y determine si comienza con la letra 'H' y no contiene la letra 'a'.")
texto = str(input("Escribe una cadena de texto: "))
if 'H' in texto[0] and 'a' not in texto:
    print("Sí, los dos requisitos se cumplen")
else:
    print("No, al menos uno de los dos requisitos no se cumplen")

print("- Escribir un programa que lea tres números enteros y determine si al menos uno de ellos es mayor que 10.")
num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce un número entero: "))
num3 = int(input("Introduce un número entero: "))
if num1 > 10 or num2 > 10 or num3 > 10:
    print("Sí, al menos uno de ellos es mayor que 10")
else:
    print("No, ninguno de ellos es mayor que 10")

print("- Escribir un programa que lea una cadena de texto y determine si contiene la palabra 'Python' o la palabra 'programación'.")
texto = str(input("Escribe una cadena de texto: "))
if 'Python' in texto or 'programación' in texto:
    print("Sí, al menos una de las dos palabras está en la cadena de texto")
else:
    print("No, ninguna de las palabras se encuentra en la cadena de texto")
