    ### Diccionarios ###

        #! Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre":"Oscar",
    "Apellido":"Flores",
    "Edad":50,
    1: "Python"
    }
my_dict = {"Nombre": "Oscar", "Apellido": "Flores", "Edad": 50,"Lenguajes": {"Python", "C","Java"},1:1.88}

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

        #!  Busqueda

print(my_dict[1])
print(my_dict["Nombre"])#   Solo muestra el valor de la clave solicitada.
print(my_dict["Lenguajes"])
print("Python" in my_dict)
print("Apellido" in my_dict)

        #!  Inserción

my_dict["Calle"]="Calle Gerion"
print(my_dict)

        #!  Actualización

my_dict["Nombre"]="Pedro"
print(my_dict)

        #!  Eliminar

del my_dict["Calle"]
print(my_dict)

        #!  Otras operaciones

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
value = my_dict.pop(1)
print(value)
print(my_dict)
my_dict.popitem()
print(my_dict)
my_dict = {'Nombre': 'Pedro', 'Apellido': 'Flores', 'Edad': 50, 'Lenguajes': {
    'Java', 'Python', 'C'}, 1: 1.88, 'Calle': 'Calle Gerion'}
del my_dict["Calle"]
print(my_dict)

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))
print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_dict))