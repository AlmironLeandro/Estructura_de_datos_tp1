# Escribir un programa que imprima por pantalla todas las fichas del domino, una por
# linea, sin repetir
def ficha():
   contador=0
   for i in range(1, 7):
        for j in range(i, 7):
            contador+=1
            print("|_ {} _|_ {} _|".format(i, j),"----> Ficha n°",(contador)) 
ficha()