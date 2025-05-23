#1
print("- Crea un diccionario con las claves 'manzana', 'naranja' y 'plátano'. Luego, utiliza el método get para obtener el valor correspondiente a la clave 'manzana'.")
frutas = {'manzana': 2, 'naranja': 3, 'plátano': 5}
print(frutas.get("manzana"))

#2
print("- Crea un diccionario con las claves 'uno', 'dos' y 'tres', y establece sus valores predeterminados en 1, 2 y 3, respectivamente. Luego, utiliza el método setdefault para agregar una nueva clave 'cuatro' con un valor predeterminado de 4.")
numeros = {'uno': 1, 'dos': 2, 'tres': 3}
numeros.setdefault("cuatro", 4)
print(numeros)

#3
print("- Crea un diccionario con las claves 'nombre' y 'edad', y establece sus valores predeterminados en 'Juan' y 30, respectivamente. Luego, utiliza el método update para cambiar el valor de la clave 'edad' a 35.")
persona = {'Nombre': 'Juan', 'Edad': 30}
persona.update({'Edad': 35})
print(persona)

#4
print("- Crea un diccionario con las claves 'manzana', 'naranja' y 'plátano', y establece sus valores predeterminados en 2, 3 y 4, respectivamente. Luego, utiliza el método pop para eliminar la clave 'naranja'.")
frutas = {'manzana': 2, 'naranja': 3, 'plátano': 4}
frutas.pop('naranja')
print(frutas)

#5
print("- Crea un diccionario con las claves 'nombre' y 'edad', y establece sus valores predeterminados en 'Juan' y 30, respectivamente. Luego, utiliza el método get para obtener el valor correspondiente a la clave 'peso'. Si la clave no existe, establece su valor predeterminado en 70.")
persona = {'Nombre': 'Juan', 'Edad': 30}
persona.setdefault("Peso", 70)
print(persona.get("Peso"))

#6
print("- Crea dos diccionarios, ventas1 y ventas2, con las claves 'enero', 'febrero' y 'marzo'. Establece los valores predeterminados en 100, 200 y 300 para ventas1, y en 150, 250 y 350 para ventas2. Luego, utiliza el método update para agregar los valores de ventas1 a ventas2.")
ventas1 = {'enero': 100, 'febrero': 200, 'marzo': 300}
ventas2 = {'enero': 150, 'febrero': 250, 'marzo': 350}
ventas2.update(ventas1)
print(ventas2)

#7
print("- Crea un diccionario con las claves 'manzana', 'naranja' y 'plátano', y establece sus valores predeterminados en 2, 3 y 4, respectivamente. Luego, utiliza un bucle for para imprimir cada clave y su valor correspondiente en una línea separada.")
frutas = {'manzana': 2, 'naranja': 3, 'plátano': 4}
for clave,valor in frutas.items():
    print(clave, valor)

#8
print("- Crea un diccionario con las claves 'a', 'b' y 'c', y establece sus valores predeterminados en 1, 2 y 3, respectivamente. Luego, utiliza el método popitem para eliminar un elemento aleatorio del diccionario.")
letras = {'a': 1, 'b': 2, 'c': 3}
letras.popitem()
print(letras)

#9
print("- Crea un diccionario con las claves 'nombre' y 'edad', y establece sus valores predeterminados en 'Juan' y 30, respectivamente. Luego, utiliza el método clear para eliminar todos los elementos del diccionario.")
persona = {'Nombre': 'Juan', 'Edad': 30}
persona.clear()
print(persona)