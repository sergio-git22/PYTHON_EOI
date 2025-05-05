#Imprimir la longitud de un string
print("- Vamos a ver la cantidad de letras que tiene una palabra o frase")
texto = "hogar"
print(len(texto))

#Imprimir un substring de un string
print("- Vamos a mostrar un substring de un string")
texto = "teléfono"
print(texto[0:3])

#Concatenar dos strings
print("- Vamos a concatenar dos strings")
texto1 = "Hola"
texto2 = "qué tal estás"
print(texto1, texto2)

#Reemplazar un substring dentro de un string
print("- Vamos a reemplazar un substring dentro de un string")
texto = "Hola cómo estás"
texto_nuevo = texto.replace("qué", "dónde")
print(texto_nuevo)

#Convertir un string a mayúsculas
print("- Vamos a pasar un string a mayúsculas")
palabra = "ordenador"
palabra_mayus = palabra.upper()
print(palabra_mayus)

#Convertir un string a minúsculas
print("- Vamos a pasar un string a minúsculas")
palabra = "ORDENADOR"
palabra_minus = palabra.lower()
print(palabra_minus)

#Dividir un string en una lista de substrings
print("- Vamos a dividir un string en una lista de substrings")
texto = "Hace,buen,día"
subtexto = texto.split(",")
print(subtexto)

#Eliminar los espacios en blanco al principio y al final de un string
print("- Vamos a eliminar los espacios en blanco al principio y al final de un string")
texto = "   Estoy trabajando   "
texto_sin_espacios = texto.strip()
print(texto_sin_espacios)

#Verificar si un substring está presente en un string
print("- Vamos a comprobar si un substring está en un string")
texto = "Estoy estudiando desarrollo web"
if "desarrollo" in texto:
    print("Sí, el substring está presente")
else:
    print("No, el substring no está presente")

#Imprimir un string en reversa
print("- Vamos a mostrar un string al reverso")
palabra = "programación"
palabra_reverso = palabra[::-1]
print(palabra_reverso)