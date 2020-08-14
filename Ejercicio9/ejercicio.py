# Escribir un programa que pida al usuario un número entero del 1 al 7 y muestre por
# pantalla el día de la semana correspondiente. Controlar que el número se encuentre
# en el rango correcto, si no es así, informar un error. Si el número es 2 el dia es
# martes.
def diasDeLaSemana():
    semanas=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo "]
    var = input("Ingrese un numero entero del 1 al 7  ")
    if(int(var)>=1 & int(var)<=7):
        print(semanas[int(var)-1])
diasDeLaSemana()