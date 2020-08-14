# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al género y
# el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y
# los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
# programa que pregunte al usuario su inicial y género, y muestre por pantalla el grupo
# que le corresponde.

# GrupoA => mujeres con letra L ; hombre con letra ñ.
# GrupoB => todo el resto.
# grupoA=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

def divisionDeCurso():
    inicial = input("Indique su inicial")
    genero  = input("A que genero pertenece?")
    cantidad = len(inicial)
    
    if( cantidad ==1 and inicial=="l" or inicial=="L"):
        print("Perteneces al grupo A")
    elif( cantidad ==1 and inicial=="ñ" or inicial=="Ñ"):
        print("Perteneces al grupo A")
    elif  (cantidad ==1 and inicial!="ñ" and inicial!="Ñ" and inicial!="l" and inicial!="L"):
        print("Perteneces al grupo B")
    else:
        print("La inicial es solo un digito")
divisionDeCurso()