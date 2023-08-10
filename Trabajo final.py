Participantes = 10
import random
def vectores_son_iguales(Number, Comp_1):
    if len(Number) != len(Comp_1):
        return False
    for i in range(len(Number)):
        if Number[i] != Comp_1[i][0]:
            return False
    return True

Ganlot = []
Ganador = 0
Perdedor = 0
Perlot = []
Ganancias = 0
Recaudacion = []
DNI = 0
VDNI = []
def Quiniela():
    global Ganador, Perdedor, Ganancias
    for j in range(1, Participantes + 1):
        print("------------Bienvenido a la Quiniela------------")
        Nombre_Apellido = str(input("Ingrese su nombre y apellido: "))
        DNI_1 = int(input("Ingrese su D.N.I: "))
        Fecha_1 = int(input("Ingrese El Día: "))
        Fecha_2 = int(input("Ingrese El Mes: "))
        Fecha_3 = int(input("Ingrese El Año: "))
        Cfra_1 = int(input("¿Cuantas cifras desean apostar? 2, 3, 4: "))
        Menu = int(input("Ingrese 1 si desea salir: "))
        
        Numero_Ap = int(input("Ingrese el monto de la apuesta: "))
        Cupon = 1
        Number = [random.randint(1, 100) for _ in range(Cfra_1)]
        Comp_1 = []
        Recaudacion.append([Numero_Ap])
        while Cupon <= Cfra_1:
           Ingreso_1 = int(input("Ingrese Los numeros del tiket de loteria: "))
           Comp_1.append([Comp_1]) 
           Cupon += 1

        if vectores_son_iguales(Number, Comp_1):
                print("Usted gano el premio de la quiniela")
                print("Su numero de documento", DNI_1)
                print(Number, Comp_1)
                Ganador += 1
                Ganlot.append([Ganador])
                VDNI.append([DNI_1])
                print("La fecha es:", Fecha_1, "/", Fecha_2, "/", Fecha_3)
                print("La cantidad apostada es", Ingreso_1 + Ingreso_1 * 10)
        else:
                print("Usted Perdio el premio de la quiniela")
                print("Su numero de documento", DNI_1)
                print(Number, Comp_1)
                Perdedor += 1
                Perlot.append([Perdedor])
                print("La fecha es:", Fecha_1, "/", Fecha_2, "/", Fecha_3)
                print("La cantidad apostada es:",  Numero_Ap)

        
            
def Quini_6():
    global Ganador, Perdedor, Ganancias
    for j in range(1, Participantes + 1):
        print("**************Bienvenido Al Quini_6**************")
        Nombre_Apellido = str(input("Ingrese su nombre y apellido: "))
        DNI_1 = int(input("Ingrese su D.N.I: "))
        Fecha_1 = int(input("Ingrese El Día: "))
        Fecha_2 = int(input("Ingrese El Mes: "))
        Fecha_3 = int(input("Ingrese El Año: "))
        Cfra_1 = int(input("Ingrese 1 si quiere participar y 2 si quiere volver al menú principal: "))
        if Cfra_1 == 2:
                break
                Menu()
        
        Ganancias += 1
        Recaudacion.append([Numero_Ap])
        if Cfra_1 == 1:
            Numero_Ap = 400
            Number = [random.randint(1, 36) for _ in range(6)]  # Sortear 6 números
            Comp_1 = []
            for _ in range(6):
                Ingreso_1 = int(input("Ingrese un número del 1 al 36: "))
                Comp_1.append(Ingreso_1)

            if sorted(Number) == sorted(Comp_1):
                print("¡Felicitaciones! Usted ganó en Quini_6")
                print("Su número de documento:", DNI_1)
                print("Los números sorteados son:", Number)
                Ganador += 1
                Ganlot.append(Ganador)
                VDNI.append([DNI_1])
                print("La fecha es:", Fecha_1, "/", Fecha_2, "/", Fecha_3)
                print("La cantidad apostada es:", Numero_Ap * 10)
            else:
                print("Lo siento, no ganó en Quini_6")
                print("Su número de documento:", DNI_1)
                print("Los números sorteados son:", Number)
                Perdedor += 1
                Perlot.append(Perdedor)
                print("La fecha es:", Fecha_1, "/", Fecha_2, "/", Fecha_3)
                print("La cantidad apostada es:", Numero_Ap)
def Arqueo_Caja():
    recaudacion_total = sum(int(Recaudacion) for i in range(1,10))
    retencion = recaudacion_total * 0.47
    ganancia_neta = recaudacion_total - retencion
    print(f"Recaudación total:", recaudacion_total)
    print(f"Retención: ", retencion) 
    print(f"Ganancia neta para el quinielero: ", ganancia_neta)
def Comprobar_apuesta():
    ingrso_2 = int(input("Ingrese su D.N.I: "))
    VDNI
    if (ingrso_2 not in VDNI):
        print("Lamento informarle que no fue una buena apuesta\n tanto como en la loteria o el quini 6")
    else:
        print("Felicidades por haber realizado una buena apuesta!")
    
    
def Mune():
 while True:
  print("***********************************************************")
  print("¡quiniela! 'La Suerte'")
  print("***********************************************************")
  print("-----------------------------------------------------------")
  print("1_ quiniela")
  print("2_ quini-6 ")
  print("3_ Comprobar apuesta")
  print("4_ Arqueo de caja")
  print("5_ Salir")
  Menu_1 = int(input("Ingrese una opcion: "))
  print("-----------------------------------------------------------")
  if Menu_1 == 1:
     Quiniela()
  elif Menu_1 == 2:
     Quini_6()
  elif Menu_1 == 3:
     Arqueo_Caja()
  elif Menu_1 == 4:
     Comprobar_apuesta()
  elif Menu_1 == 5:
      break      
  
Mune()

    
