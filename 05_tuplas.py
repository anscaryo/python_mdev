    ### tuplas ###
#?  Los valores de una tupla, no se pueden modificar despues de crearlos.


mi_tupla = tuple()
otra_tupla = ()

mi_tupla = (50, 1.88, "Oscar", "Flores", "Oscar")
otra_tupla = (35, 32, 69, 87)
print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[0])
print(mi_tupla[-1])

print(mi_tupla.count("Oscar"))# Cuenta el numero de elementos que coinciden con el solicitado
print(mi_tupla.index("Flores"))
print(mi_tupla.index("Oscar"))

#  mi_tupla[1] = 1.80   #!  TypeError: 'tuple' object does not support item assignment

print(mi_tupla + otra_tupla)

        #!  Concatenación

suma_tuplas = mi_tupla + otra_tupla
print(suma_tuplas)

        #!  Subtuplas

print(suma_tuplas[3:6])

        #!  tupla mutable con conversión a lista
'''
    Convierte una tupla en una lista para poder modificar los valores de la tupla
    al terminar lo convierte en tupla otra vez
'''
mi_tupla = list(mi_tupla)

print(type(mi_tupla))

mi_tupla[4] = "Anscaryo"
mi_tupla.insert(1, "Azul")
mi_tupla = tuple(mi_tupla)
print(type(mi_tupla))
print(mi_tupla)

        #!  Eliminación

#  del mi_tupla[2]  #! TypeError: 'tuple' object doesn't support item deletion
del mi_tupla
#print(mi_tupla)  #! NameError: name 'mi_tupla' is not defined
