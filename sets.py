#1
print("- Crea un set vacío y luego agrega los números del 1 al 5.")
numeros = set()
for i in range(1, 6):
    numeros.add(i)
print(numeros)

#2
print("- Crea un set con los nombres de tus compañeros de clase y luego muestra la cantidad de elementos que tiene.")
compis = {'Ana', 'Silvia', 'Richard'}
print(len(compis))

#3
print("- Crea dos sets con los números del 1 al 5 y del 4 al 8, y muestra la unión entre ellos.")
s1 = set(range(1, 6))
s2 = set(range(4, 9))
print(s1.union(s2))
#print(s1 | s2)

#4
print("- Crea un set con los números del 1 al 10 y elimina el 5.")
numeros = set(range(1, 11))
numeros.remove(5)
print(numeros)

#5
print("- Crea dos sets con los números del 1 al 5 y del 3 al 7, y muestra la intersección entre ellos.")
s1 = set(range(1, 6))
s2 = set(range(3, 8))
print(s1.intersection(s2))
#print(s1 & s2)

#6
print("- Crea un set con los números del 1 al 10 y muestra los números pares que contiene.")
numeros = set(range(1, 11))
for i in numeros:
    if i % 2 == 0:
        print(i)

#7
print("- Crea un set con los nombres de los días de la semana y muestra los días que comienzan con la letra 'M'.")
dias = {'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'}
dias_m = {d for d in dias if d.startswith('M')}
print(dias_m)

#8
print("- Crea un set con los números del 1 al 5 y luego agrega el número 6.")
numeros = set(range(1, 6))
numeros.add(6)
print(numeros)

#9
print("- Crea dos sets con los números del 1 al 5 y del 4 al 8, y muestra la diferencia entre ellos.")
s1 = set(range(1, 6))
s2 = set(range(4, 9))
print(s1.difference(s2))

#10
print("- Crea un set con los nombres de tus compañeros de clase y verifica si tu nombre está en el set.")
compis = {'Ana', 'Silvia', 'Richard'}
if 'Sergio' in compis:
    print("Sí")
else:
    print("No")

#11
print("- Crea dos sets con los números del 1 al 5 y del 4 al 8, y muestra los números que se encuentran en ambos sets.")
s1 = set(range(1, 6))
s2 = set(range(4, 9))
print(s1.intersection(s2))

#12
print("- Crea un set con los nombres de tus compañeros de clase y agrega tu propio nombre al final.")
compis = {'Ana', 'Silvia', 'Richard'}
compis.add('Sergio')
print(compis)

#13
print("- Crea un set con los números del 1 al 10 y muestra los números impares que contiene.")
numeros = set(range(1, 11))
for i in numeros:
    if i % 2 != 0:
        print(i)

#14
print("- Crea un set con los nombres de los días de la semana y muestra los días que terminan con la letra 's'.")
dias = {'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'}
dias_s = {d for d in dias if d.endswith('s')}
print(dias_s)

#15
print("- Crea dos sets con los números del 1 al 5 y del 3 al 7, y muestra la unión simétrica entre ellos.")
s1 = set(range(1, 6))
s2 = set(range(3, 8))
print(s1.symmetric_difference(s2))

#16
print("- Crea un set con los nombres de tus compañeros de clase y otro set con los nombres de tus amigos fuera de clase. Luego muestra los nombres que se encuentran en ambos sets.")
compis = {'Ana', 'Silvia', 'Richard'}
amigos = {'Javi', 'Nerea', 'Alex'}
comun = compis.intersection(amigos)
print(comun)

#17
print("- Crea un set con los números del 1 al 10 y verifica si el set está vacío.")
numeros = set(range(1, 11))
if numeros:
    print("El set no está vacío")
else:
    print("El set está vacío")

#18
print("- Crea dos sets con los números del 1 al 5 y del 4 al 8, y muestra la diferencia simétrica entre ellos.")
s1 = set(range(1, 6))
s2 = set(range(4, 9))
print(s1.symmetric_difference(s2))
#print(s1 ^ s2)

#19
print("- Crea un set con los nombres de tus compañeros de clase y muestra los nombres en orden alfabético.")
compis = {'Ana', 'Silvia', 'Richard'}
print(sorted(compis))

#20
print("- Crea un set con los números del 1 al 10 y verifica si el set contiene todos los números del 1 al 5.")
numeros = set(range(1, 11))
subset = set(range(1, 6))

if subset.issubset(numeros):
    print("Sí, están")
else:
    print("No, no están")
