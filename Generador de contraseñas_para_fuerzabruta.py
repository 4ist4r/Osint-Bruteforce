#Generador de contraseñas 
import random
print("GENERADOR DE CONTRASEÑAS BY AIST4R")
#Recopilacion de datos para la libreria
#nombre
print("inserte nombre:   ") 
nombre=input("")
#apellidos
print("inserte apellidos:   ") 
apellidos=input("")
#nombre de los padres
print("inserte nombres de progenitores: ") 
print("nombre del padre")
nombre_de_padre=input("")
print("nombre de la madre")
nombre_de_madre=input("")
#nombre de hermanos 
print("inserte nombre de hermanos") 
hermanos=input("")
#nombre de mascotas
print("inserte nombre de  mascota ") 
mascota=input("")
#fecha de nacimiento 
print("ingrese fecha de nacimiento")
nacimiento=input("")

#datos recopilados 

datos = {nombre, apellidos, nombre_de_padre, nombre_de_madre, hermanos, mascota, nacimiento}
print (datos)

#guardar libreria de datos (sin mezclar) recopilados
with open("datos.txt", "w") as archivo:
    for clave, valor in datos.item():
        archivo.write(f"{clave}: {valor}\n")

#hacer creacion de libreria para fuerza bruta
random.shuffle(datos)
print(datos)

# guardar libreria
with open("libreria.txt", "w") as archivo:
    for clave, valor in datos.item():
        archivo.write(f"{clave}: {valor}\n")

