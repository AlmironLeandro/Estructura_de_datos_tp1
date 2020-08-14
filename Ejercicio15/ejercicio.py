# Ejercicio 15
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un
# triángulo rectángulo como el de más abajo, de altura igual al número introducido
def triangulo():
    columnaYfila()

def fila(numero):
    var = 1
    ast = "*"
    while numero >= var:
        var+=1
        print (ast, end = '')

def columnaYfila():
    dato = input("Ingrese la altura  ")
    contador = 0
    while  contador < int(dato):
        fila(contador)
        print("*")
        contador+=1


        
triangulo()
