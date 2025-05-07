#1
print("- Imprimir la longitud de un string.")
texto = "hogar"
print(len(texto))

#2
print("- Imprimir un substring de un string.")
texto = "teléfono"
print(texto[0:3])

#3
print("- Concatenar dos strings.")
texto1 = "Hola"
texto2 = "qué tal estás"
print(texto1, texto2)

#4
print("- Reemplazar un substring dentro de un string.")
texto = "Hola cómo estás"
texto_nuevo = texto.replace("qué", "dónde")
print(texto_nuevo)

#5
print("- Convertir un string a mayúsculas.")
palabra = "ordenador"
palabra_mayus = palabra.upper()
print(palabra_mayus)

#6
print("- Convertir un string a minúsculas.")
palabra = "ORDENADOR"
palabra_minus = palabra.lower()
print(palabra_minus)

#7
print("- Dividir un string en una lista de substrings.")
texto = "Hace,buen,día"
subtexto = texto.split(",")
print(subtexto)

#8
print("- Eliminar los espacios en blanco al principio y al final de un string.")
texto = "   Estoy trabajando   "
texto_sin_espacios = texto.strip()
print(texto_sin_espacios)

#9
print("- Verificar si un substring está presente en un string.")
texto = "Estoy estudiando desarrollo web"
if "desarrollo" in texto:
    print("Sí, el substring está presente")
else:
    print("No, el substring no está presente")

#10
print("- Imprimir un string en reversa.")
palabra = "programación"
palabra_reverso = palabra[::-1]
print(palabra_reverso)