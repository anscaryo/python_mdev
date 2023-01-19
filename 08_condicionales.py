    ### Condicionales ###

#   if

condicion = False

if condicion:
    print("se ejecuta la condicion del if.")

condicion = 5*2

if condicion == 10:
    print("Se ejecuta la condición del segundo if.")
# if, elif, else

condicion = 5*5+1

if condicion > 10 and condicion < 20:
    print("ES mayor que 10 y menor que 20.")
elif condicion == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25.")

print("El programa continua.".center(100, "·"))

#   condicional con inspeccion de valor

my_string = ""

if not my_string:
    print ("Mi canena de texto esta vacia.")
if my_string == "Mi cadena de textoooooo.":
    print("Estas cadenas de texto coinciden.")