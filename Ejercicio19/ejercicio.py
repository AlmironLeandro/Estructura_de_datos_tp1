# Ejercicio 19
# Escribir un programa que recibe como entrada desde el usuario dos números enteros
# e informa por pantalla todos los números pares entre ellos.
def numerosN():
    val1 = int(input("Ingrese un numero "))+1
    val2 = int(input("Ingrese otro numero "))+1
    if val1 > val2:
        while val2 < val1: 
            if val2%2==0 and not(val2 == val1):
                print(val2)
            val2+=1
    else:
        while val1 < val2:
            if val1%2==0:
                print(val1)
            val1+=1

numerosN()