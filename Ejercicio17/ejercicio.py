# Ejercicio 17
# Escribir un programa que pida un número natural n al usuario e imprima por pantalla
# la suma de los números naturales de 1 hasta n. Por ejemplo para n = 5, la salida debe
# ser:
# 1 + 2 + 3 + 4 + 5 = 15
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

# def prueba1(numero):
#         var = 0
#         nam = numero
#         if(var == numero):
#             return 0
#         else:
#             var+=1
#             prueba1(nam + var)
#         return numero

def sumaNumeroNat():
    valor = input("Ingrese un numero natural ")
    contador = 0
    suma = int(valor)
    while int(valor)> contador :
        suma +=contador
        contador+=1
        print(suma)

sumaNumeroNat()
# prueba1(3)