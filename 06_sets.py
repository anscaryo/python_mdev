        ### Sets ###

    #!  Definición

mi_set = set()
mi_otra_set = {}

print(type(mi_set))
print(type(mi_otra_set))#?  Inicialmente es un diccionario.

mi_otra_set = {"Oscar", "Flores", 50}
print(type(mi_otra_set))

print(len(mi_otra_set))

        #!  Inserción

mi_otra_set.add("Anscaryo")
print(mi_otra_set)# Un set no es una estructura ordenada

mi_otra_set.add("ansgair")
print(mi_otra_set)

mi_otra_set.add("ansgair")# no admite repetidos.
print(mi_otra_set)

        #!  Búsquedas

print("ansgair" in mi_otra_set)
print("ans_gair" in mi_otra_set)

        #!  Eliminación

mi_otra_set.remove("ansgair")
print("ansgair" in mi_otra_set)

mi_otra_set.clear()
print(len(mi_otra_set))

del mi_otra_set
#print(mi_otra_set)  # !    NameError: name 'mi_otra_set' is not definedo

        #!  Transformaciones

mi_set = {"Oscar", "Flores", 50}
mi_lista = list(mi_set)
print(mi_lista)
print(mi_lista[1])

mi_otra_set = {"Kotlin","Swift", "Python"}

        #!  Otras operaciones

mi_nuevo_set = mi_set.union(mi_otra_set)
print(mi_nuevo_set)
print(mi_nuevo_set.union(mi_nuevo_set).union({"JavaScripot", "C#"}))
print(mi_nuevo_set.difference(mi_set))