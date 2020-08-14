# Ejercicio 12
# Mostrar por pantalla todos los números enteros entre 1 y 100, hacerlo usando un
# bucle while y tambien con un bucle for.

def primerBucle():
    i = 1
    while (i<=100):
        print(i)
        i+=1


def segundoBucle():
    for i in range(1,101):
        print(i)

segundoBucle()