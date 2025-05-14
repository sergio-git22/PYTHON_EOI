#1
print("- Escribe un programa que cree un diccionario con las edades de 5 personas y luego imprima el diccionario.")
personas = {'Adrián': 43, 'Laura': 35, 'Carlos': 12, 'Marta': 27, 'Saúl': 7}
print(personas)

#2
print("- Escribe un programa que cree un diccionario vacío y luego pida al usuario introducir nombres y edades hasta que el usuario introduzca 'fin'. Luego, imprime el diccionario.")
dic = {}
while True:
    nombre = str(input("Escribe un nombre: "))
    if nombre == 'fin':
        break
    edad = int(input("Escribe la edad de " + nombre + ": "))
    dic[nombre] = edad
print(dic)

#3
print("- Escribe un programa que cree un diccionario con las notas de 3 alumnos y luego calcule y muestre la media de las notas.")
notas = {'Juan': 7, 'Lucía': 9, 'Teresa': 5}
media = sum(notas.values()) / len(notas)
print("La media de las notas de los alumnos es", media)

#4
print("- Escribe un programa que cree un diccionario con los precios de 3 productos y luego calcule y muestre el precio total de la compra.")
productos = {'manzana': 2, 'naranja': 4, 'plátano': 3}
total = sum(productos.values())
print("El precio total de los productos es", total)

#5
print("- Escribe un programa que cree un diccionario con los nombres y edades de 3 personas y luego ordene el diccionario por edad y lo imprima.")
personas = {'Roberto': 31, 'Diana': 20, 'Francisco': 59}
personas_ordenadas = dict(sorted(personas.items(), key=lambda item: item[1]))
print(personas_ordenadas)

#6
print("- Escribe un programa que cree un diccionario con los nombres y alturas de 3 personas y luego calcule y muestre la altura media.")
alturas = {'Tomás': 1.75, 'Juana': 1.64, 'Paloma': 1.72}
media = sum(alturas.values()) / len(alturas)
print("La altura media de Tomás, Juana y Paloma es", media)

#7
print("- Escribe un programa que cree un diccionario con las notas de 3 alumnos y luego elimine la nota del alumno con la nota más baja. Luego, imprime el diccionario.")
notas = {'Sergio': 10, 'Carla': 6, 'Vicente': 8}
peor_alumno = min(notas, key=notas.get)
del notas[peor_alumno]
print(notas)

#8
print("- Escribe un programa que cree un diccionario con los nombres y edades de 3 personas y luego pida al usuario introducir un nombre y una nueva edad para esa persona. Si el nombre existe en el diccionario, actualiza la edad y muestra el diccionario actualizado. Si el nombre no existe, muestra un mensaje de error.")
personas = {'Gonzalo': 34, 'Bárbara': 22, 'Raúl': 13}
nombre = str(input("Escribe un nombre: "))
if nombre in personas:
    edad = int(input("Actualiza la edad de " + nombre + ": "))
    personas[nombre] = edad
    print(personas)
else:
    print("El nombre no existe en el diccionario")

#9
print("- Escribe un programa que cree un diccionario con los nombres y edades de 3 personas y luego muestre solo los nombres que empiezan por 'M'.")
personas = {'Unai': 39, 'Leire': 31, 'Mikel': 34}
for persona in personas:
    if persona.startswith("M"):
        print(persona)