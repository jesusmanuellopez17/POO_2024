"""

existe una estructura de condicion lla mada "if"
la cual evalua una condicion para encontrar el valoe "True" y si se cumple
la condicion se ejecuta la linea o lineas de codigo

tienes 4 variantes de if 

1.-if  simple
2.-if compuesto
3.-if anidado
4.-if y elif

"""


""""

##Ejemplo 1 if simple

color=input("Ingresa un color")

if color == "rojo":
    print("Soymel color rojo")

#Ejemplo 2 if compuesto

color=input("Ingresa un color")

if color == "rojo":
    print("Soymel color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#Ejemplo 3 if anidado

color=input("Ingresa un color")

if color == "rojo":
    print("Soy el color rojo")
    if color!="rojo":
        print("Soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#Ejemplo 4 if y elif

color=input("Ingresa un color")

if color == "rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo")
elif color=="azul":
    print("Soy el color azul")
elif color=="morado":
    print("Soy el color morado")
else:
    print("No soy ningun de los anteriores")


"""


# Ejemplo 5 Crear un programa que solicite el numero de la semana
#e imprima en pantalla el dia que le corresponde

dia_semana =  input  ("Ingrese el numero de la semana")

if dia_semana == 1:
 print ("Soy el dia Lunes")
elif dia_semana == 2:
    print ("Soy el Dia  Martes")
elif dia_semana == 3:
    print ("Soy el Dia Miercoles ")
elif dia_semana == 4:
    print ("Soy el Dia Jueves")
elif dia_semana == 5 :
    print ("Soy el Dia Viernes")


