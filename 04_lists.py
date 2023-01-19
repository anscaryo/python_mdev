### Lists ###

#!   Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,24,62,52,30,30,17]

print(f"Contenido de my_list: {my_list}")
print(len(my_list))

my_other_list = [50, 1.78, "Oscar", "Flores"]

print(type(my_list))
print(type(my_other_list))

#!  Aceeso a elementos y busqueda.

print(my_other_list[0])#    Accede al primer elemento
print(my_other_list[1])#    Accede al segundo elemento
print(my_other_list[-1])  # Accede al primer elemento empezando por el final
print(my_other_list[-4])#   Accede al cuarto elemento empezando por el final
print(my_list.count(30))#   cuenta cuantos "30" hay en la lista my_list
#print(my_other_list[4])  # !IndexError list index out of range
print(my_other_list.index("Oscar"))

edad, altura, nombre, apellido = my_other_list
print(nombre)

nombre, altura, edad, apellido = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(edad)

#!  Concatenación

print(my_list + my_other_list)

#!  Ceración, inserción, actualización y eliminación

my_other_list.append("Anscaryo") #  añade un elemento al final de la lista.
print(my_other_list)

my_other_list.insert(1, "Tecnico")# añade un elemento en la posición indicada.
print(my_other_list)

my_other_list[1] = "Azul"#  asigna un valor a la posición indicada de la lista.
print(my_other_list)

my_list.remove(30)# borra el elemento que coincide con el indicado. Solo uno.
print(my_list)

print(my_list.pop())#   Extrae el ultimo de la lista.
print(my_list)

my_pop_element = my_list.pop(2)#    Extrae el elemento en la posicion indicada y se lo asigna a una variable.
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

#!  Operaciones con listas

my_new_list = my_list.copy()#   Copia el contenido de una lista en otra.
my_list.clear()#    Limpia el contenido de la lista.
print(my_list)
print(my_new_list)

my_new_list.reverse()#  revierte el orden de la lista.
print(my_new_list)

my_new_list.sort()# Ordena el contenido de la lista ascendente.
print(my_new_list)

my_new_list.sort(reverse=True)  # Ordena el contenido de la lista descendente.
print(my_new_list)

#!  Cambio de tipo.

print(type(my_list))
my_list = "Hola Python"
print(type(my_list))
print(my_list)