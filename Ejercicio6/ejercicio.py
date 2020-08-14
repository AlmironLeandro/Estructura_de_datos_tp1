# Escribir un programa pida al usuario dos numeros enteros e informe por pantalla cual
# es menor de los dos, si son iguales, indicarlo por separado.
def numeros():
    numero1 =input("ingrese un numero")
    numero2 = input("ingrese otro numero")
    if(numero1<numero2):
        print("El primer numero es menor al segundo")
    elif(numero1==numero2):
        print("Ambos numeros son iguales")
    elif(numero2<numero1):
        print("El segundo numero es menor al primero")

numeros()