# Escribir un programa para una empresa que tiene salas de juegos para todas las
# edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes
# por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el
# precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene
# entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10.

def pagarEntrada():
    edad = input("Que edad tenes?  ")
    if(int(edad)<=4):
        print("It´s free!")
    elif(int(edad)>4 and int(edad)<=18):
        print("Debe abonar $5")
    elif (int(edad)>18):
        print("Debe abonar $10")
pagarEntrada()