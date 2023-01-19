### String  ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de liena"
print(my_new_line_string)

my_tab_string = "\tESte es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

#   Formateo

name, surname, age = "Oscar", "Flores", 50
print("Mi nombre es {} {} y mi edad es {}.".format(name, surname,age))
print("Mi nombre es %s %s y mi edad es %d."%(name, surname,age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)+".") # !, esta forma no es la más correcta, es muy trabajosa.
print(f"mi nombre es {name} {surname} y mi edad es {age}.")# *, inferencia de datos.

#   Desempaqueado de caracteres

language = "phthon"
a,b,c,d,e,f = language
print(a)
print(e)

#   División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#   Funciones del lenguaje

print(language.capitalize())#   la primera mayuscula
print(language.upper())#    escribe en mayusculas
print(language.count("t"))# cuentas el numero de letras indicadas estan en el string
print(language.isnumeric())#    Indica si es un numero
print("1".isnumeric())  # Indica si es un numero
print(language.lower())#    escribe en minusculas
print(language.lower().isupper())#  comprueba si esta en mayusculas
print(language.startswith("Py"))#   comprueba si enmpieza por ""
print("Py" == "py") # No es lo mismo