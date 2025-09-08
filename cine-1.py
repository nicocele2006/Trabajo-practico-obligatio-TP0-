#import 

def selec_peli():
    print ("Las peliculas que proyectamos son:")

    for i in range(0, len(peliculas)):
        print(str(i+1) + ". - " + peliculas[i])

    pelicula_selec = -1
    while pelicula_selec < 0 or pelicula_selec > len(peliculas):
        try:
            pelicula_selec = int(input("Selecione la pelicula: "))
            print ("Selecionaste " + peliculas[pelicula_selec-1])
        except ValueError:
            print("Valor no es entero")
        except IndexError:        
            print ("Valor fuera de rango")
    return pelicula_selec

def selec_dia():
        
    for i in range(0, len(dias)):
        print(str(i+1) + ". - " + dias[i])

    dia_elegido = -1
    while dia_elegido < 0 or dia_elegido > len(dias):
        try:
            dia_elegido = int(input("Selecione el dia: "))
            print ("Selecionaste " + dias[dia_elegido-1])
        
        except ValueError:
            print("Valor no es entero")
        except IndexError:        
            print ("Valor fuera de rango")
    return dia_elegido

def selec_hora():
    for i in range(0, len(horarios)):
        print(str(i+1) + ". - " + horarios[i])

    horario_elegido = -1
    while horario_elegido < 0 or horario_elegido > len(horarios):
        try:
            horario_elegido = int(input("Selecione el horario: "))
            print ("Selecionaste " + horarios[horario_elegido-1])

        except ValueError:
            print("Valor no es entero")
        except IndexError:        
            print ("Valor fuera de rango")
    return horario_elegido

def elegir_asiento():
    fila0 = [1,1,0,0] 
    fila1 = [0,0,1,0]
    fila2 = [0,1,0,0]
    sala = [fila0,fila1,fila2]

    cant_asientos = len(sala[0])
    leyenda_sup = ""
    for i in range(0, cant_asientos):
        leyenda_sup = leyenda_sup + "A"+str(+i+1)+"  "
    print("        " + leyenda_sup)

    for fila in range(0, len(sala)):
        print ("Fila "+str(fila+1)+": ", end=" ")
        for colum in range(0,len(sala[fila])):
            if colum < len(sala[fila]) -1:
                print(sala[fila][colum], end="   ")
            else:
                print(sala[fila][colum])

    print()    
    asientovalido = False
    while not asientovalido:
        usuario_fila = int(input("Ingrese fila: "))
        usuario_columna = int(input("Ingrese columna: "))
        asiento = sala[usuario_columna-1][usuario_columna-1]
        if asiento == 0:
            asientovalido = True
        else:
            print("Butaca ocupada, selecione otra.")

    print("Has reservado tu butaca correctamente")

    sala[usuario_columna-1][usuario_columna-1] = 1
    return



print ("Bienvenido al Sistema de tickets Cine Uade")
print("")

entrada = True
while entrada:
    usuarios = ["nico|66","olimar|89","lautaro|12"]

    entrar_usuario = input("Ingrese su usuario: ")
    entrar_contraseña = input("Ingrese su contraseña: ")
    if usuarios.count(entrar_usuario+"|"+entrar_contraseña):
        print ("Bienvenido ", entrar_usuario)
        entrada = False
    else:
        print ("usuario o contraseña incorrecta vuelve a intentarlo")


peliculas = ["Los 4 Fantasticos", "It", "Superman", "El conjuro"]
dias = ["Martes", "Miercoles", "Jueves", "Sabado"]
horarios = ["13:00","15:00","16:30","21:00"]
ciclodereservas = True
while ciclodereservas:
    pelicula_selec = selec_peli()
    #--------------------------------
    dia_selec = selec_dia()
    #---------------------------------
    hora_selec = selec_hora()
    #------------------------------------------------
    asiento_selec = elegir_asiento()
    masentrada = input("Quiere otra reserva?, si es asi presione S: ")
    if masentrada.lower == "s":
        ciclodereservas = True
    else:
        ciclodereservas = False


