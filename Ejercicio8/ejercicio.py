# Escribir un programa que pida al usuario un número entero e indique si dicho número
# es par o impar.
def isPar():
    var = input("Ingrese numero entero  ")
    if(int(var)%2==0 ):
        print("ES PAR!")
    else:
        print("Es INPAR")
isPar()