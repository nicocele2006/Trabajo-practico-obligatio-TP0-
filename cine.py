#import 
fila0 = [1,1,0,0] 
fila1 = [0,0,1,0]
fila2 = [0,1,0,0]
sala = [fila0,fila1,fila2]

peliculas = ["Los 4 Fantasticos", "It", "Superman", "El conjuro"]
dias = ["Martes", "Miercoles", "Jueves", "Sabado"]
horarios = ["13:00","15:00","16:30","21:00"]

print ("Bienvenido al Sistema de tickets Cine Uade")
print("")
print ("Las peliculas que proyectamos son:")

for i in range(0, len(peliculas)):
    print(str(i+1) + ". - " + peliculas[i])

pelicula_selec = -1
while pelicula_selec < 0 or pelicula_selec > len(peliculas):

    pelicula_selec = input("Selecione la pelicula: ")
    if(pelicula_selec.isdigit()):
        pelicula_selec = int(pelicula_selec)
    else:
        pelicula_selec = -1        

    if pelicula_selec > 0 and pelicula_selec < len(peliculas):
        print ("Selecionaste " + peliculas[pelicula_selec-1])
    else:
        print("Valor fuera de rango")
#--------------------------------

for i in range(0, len(dias)):
    print(str(i+1) + ". - " + dias[i])

dia_elegido = -1
while dia_elegido < 0 or dia_elegido > len(dias):

    dia_elegido = input("Selecione el dia: ")
    if(dia_elegido.isdigit()):
        dia_elegido = int(dia_elegido)
    else:
        dia_elegido = -1        

    if dia_elegido > 0 and dia_elegido < len(dias):
        print ("Selecionaste " + dias[dia_elegido-1])
    else:
        print("Valor fuera de rango")


#---------------------------------

for i in range(0, len(horarios)):
    print(str(i+1) + ". - " + horarios[i])

horario_elegido = -1
while horario_elegido < 0 or horario_elegido > len(horarios):

    horario_elegido = input("Selecione el horario: ")
    if(horario_elegido.isdigit()):
        horario_elegido = int(horario_elegido)
    else:
        horario_elegido = -1        

    if horario_elegido > 0 and horario_elegido < len(horarios):
        print ("Selecionaste " + horarios[horario_elegido-1])
    else:
        print("Valor fuera de rango")

#------------------------------------------------


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
