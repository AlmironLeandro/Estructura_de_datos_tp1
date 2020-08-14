# Ejercicio 13
# Escribir un programa que pida al usuario dos numeros enteros e imprima todos los
# numeros enteros entre los dos.

def dosNumeros():
    primer = input("Ingrese el primer numero")
    segundo = input("Ingrese el segundo numero")
    if int(primer)> int(segundo):
        print("Entroo")
        
        while int(primer) > int(segundo):
            print (int(segundo)+1)
            int(segundo)+1


dosNumeros()
