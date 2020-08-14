# Ejercicio 14
# Escribir un programa que pregunte el nombre del usuario en la consola y un número
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
# como el número introducido.

def ejercicio14():
    nombreUsuario = input("Cual es tu nombre? ")
    numeroEntero  = input("Eliga un numero entero ")
    contador = int(numeroEntero)
    while contador >= 1:
        print(nombreUsuario)
        contador-=1

ejercicio14()    