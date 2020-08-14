# Construir un programa que lea un número natural N y calcule la suma de los primeros
# N números pares.

def sumaPares():
        numero = input("Ingrese el numero Natural  ")
        for i in range(int(numero)):
            if i%2:
                print(i+1,"es par")

sumaPares()                