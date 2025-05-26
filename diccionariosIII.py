#1
print("- Crea un diccionario con los siguientes valores: 'manzana': 2, 'naranja': 3, 'banana': 1. Imprime los items del diccionario.")
frutas = {'manzana': 2, 'naranja': 3, 'banana': 1}
print(frutas.items())

#2
print("- Utiliza el método keys para imprimir las claves del diccionario del ejercicio anterior.")
print(frutas.keys())

#3
print("- Utiliza el método values para imprimir los valores del diccionario del ejercicio anterior.")
print(frutas.values())

#4
print("- Crea una copia del diccionario del ejercicio anterior y muéstrala por pantalla.")
frutas2 = frutas.copy()
print(frutas2)

#5
print("- Crea un nuevo diccionario con las claves 'manzana', 'naranja' y 'banana', y un valor de 0 para cada una. Utiliza el método fromkeys para hacerlo.")
frutas_nuevas = dict.fromkeys(['manzana', 'naranja', 'banana'], 0)
print(frutas_nuevas)

#6
print("- Agrega una nueva clave-valor al diccionario del ejercicio 1: 'pera': 4. Imprime el diccionario actualizado.")
frutas.setdefault('pera', 4)
#frutas["pera"] = 4
print(frutas)

#7
print("- Utiliza el método get para obtener el valor asociado a la clave 'manzana' en el diccionario del ejercicio 1.")
print(frutas.get('manzana'))

#8
print("- Utiliza el método pop para eliminar la clave-valor asociada a la clave 'banana' en el diccionario del ejercicio 1. Imprime el diccionario actualizado.")
frutas.pop('banana')
print(frutas)

#9
print("- Utiliza el método clear para eliminar todos los elementos del diccionario del ejercicio 1. Imprime el diccionario actualizado.")
frutas.clear()
print(frutas)

#10
print("- Crea un diccionario vacío y utiliza el método update para agregar los elementos del diccionario del ejercicio 1. Imprime el diccionario actualizado.")
dic = {}
dic.update(frutas2)
print(dic)