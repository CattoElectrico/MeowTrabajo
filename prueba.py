import csv, os, random, time

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
opc = 0
asignacionDeSueldos = False
print(len(trabajadores))
for a in range(len(trabajadores)):                          #Transforma la lista a matriz
    trabajadores[a] = [trabajadores[a]]

#----------------------------------------------------------------------Pasa la lista a una matriz---------------------------------------------------------

def mostrarTabla(lista):
    os.system("cls")
    for a in range(len(lista)):
        print(lista[a])
    input("Presione ENTER para continuar")
    
#---------------------------------------------------------------------Asigna los sueldos----------------------------------------------------------

def asignarSueldosAleatorios(lista):
    for a in range(len(lista)):
        lista[a].append(random.randint(300000,2500000))
    input("La asignacion de sueldos se ha terminado\nPresione ENTER para continuar")
    return lista

#-------------------------------------------------------------------------Clasifica los sueldos que se asignan-----------------------------------------------------

def clasificarSueldos(lista):
    sumaTotal = 0
    menor_800000 = []
    sueldo_800000_200000 = []                           #Listas que clasifican sueldos
    mayor_2000000 = []
    
    for a in range(len(lista)):                         #Mete los nombres y sueldos en la lista para cada uno
        if lista[a][1] < 800000:
            menor_800000.append(lista[a])
        elif lista[a][1] <= 2000000:
            sueldo_800000_200000.append(lista[a])
        else:
            mayor_2000000.append(lista[a])
        sumaTotal = sumaTotal + lista[a][1]             #Suma todos los sueldos
        
    print("---Sueldos menores a $800000---")
    print(f"TOTAL = {len(menor_800000)}")
    print("[nombre]     [sueldo]")
    for a in range(len(menor_800000)):
        print(f"[{menor_800000[a][0]}] [${menor_800000[0][1]}]")
        
    print("---Sueldos entre $800000 a $2000000---")
    print(f"TOTAL = {len(sueldo_800000_200000)}")
    print("[nombre]     [sueldo]")
    for a in range(len(sueldo_800000_200000)):
        print(f"[{sueldo_800000_200000[a][0]}] [${sueldo_800000_200000[0][1]}]")
        
    print("---Sueldos mayores a 2000000---")
    print(f"TOTAL = {len(mayor_2000000)}")
    print("[nombre]     [sueldo]")
    for a in range(len(mayor_2000000)):
        print(f"[{mayor_2000000[a][0]}] [${mayor_2000000[0][1]}]")
    input("Presione ENTER para seguir")
    
#-----------------------------------Muestra estadisticas de sueldo-------------------------------------------

def estadisticasDeSueldo(lista):
    sueldoMasAlto = 0
    nombre1 = ""
    sueldoMasbajo = 3000000
    nombre2 = ""
    promedio = 0
    mediaGeometrica = 1
    
    for a in range(len(lista)):                                         #Busca el sueldo mas alto
        if lista[a][1] > sueldoMasAlto:
            sueldoMasAlto = lista[a][1]
            nombre1 = lista[a][0]        
        
        #Busca el sueldo mas bajo
        if lista[a][1] < sueldoMasbajo:
            sueldoMasbajo = lista[a][1]
            nombre2 = lista[a][0]        
            
        #Suma todos los sueldos para el promedio
        promedio = lista[a][1] + promedio    
        
        #multiplica todos los sueldos para la media geometrica
        mediaGeometrica = lista[a][1] * mediaGeometrica
    
    print(f"--------Estadisticas de sueldo--------")
    print(f"Sueldo mas alto: ${sueldoMasAlto}  -  {nombre1}\nSueldo mas bajo: ${sueldoMasbajo}  -  {nombre2}\nPromedio de sueldos: ${promedio/len(lista)}\nmedia geometrica sin truncar: {(mediaGeometrica**(1/len(lista)))}\nMedia geometrica truncada: {int(mediaGeometrica**(1/len(lista)))}")
    input("Presione ENTER para seguir")
    
#------------------------------------------------------------------Muestra descuentos y los exporta a un archivo csv------------------------------------------------------

def reporteDeSueldos(lista):
    with open("Reporte de sueldos.csv", "w", newline="", encoding="utf-8") as unArchivo:
        escribir = csv.writer(unArchivo)
        escribir.writerow(["---------Reporte de sueldos---------", "\n", "Nombre", "Sueldo base", "Salud", "AFP", "Sueldo Liquido"])
        print("Nombre   Sueldo base   Salud   AFP  Sueldo Liquido")
        for a in range(len(lista)):
            escribir.writerow([f"{lista[a][0]}, ${lista[a][1]}, ${int(lista[a][1] * 0.07)}, ${int(lista[a][1] * 0.12)}, ${int(lista[a][1] - (lista[a][1] * 0.07) - (lista[a][1] * 0.012))}"])
            print(f"{lista[a][0]} ${lista[a][1]} ${int(lista[a][1] * 0.07)} ${int(lista[a][1] * 0.12)} ${int(lista[a][1] - (lista[a][1] * 0.07) - (lista[a][1] * 0.012))}")
        print("\nSe ha creado archivo 'Reporte de sueldos.csv")
        
        print("Este reporte esta truncado para mejor legibilidad. Si quiere ver los datos completos escriba 'si'")
        a = input(">").lower()
        if a == "si" or a == "s":
            print("Nombre       Sueldo base       Salud       AFP       Sueldo Liquido")
            escribir.writerow(["\n\n","---------Reporte de sueldos sin truncar---------", "\n","Nombre", "Sueldo base", "Salud", "AFP", "Sueldo Liquido"])
            for e in range(len(lista)):
                print(f"{lista[e][0]}, ${lista[e][1]}, ${lista[e][1] * 0.07}, ${lista[e][1] * 0.12}, ${lista[e][1] - (lista[e][1] * 0.07) - (lista[e][1] * 0.012)}")
                escribir.writerow([f"{lista[e][0]}, ${lista[e][1]}, ${lista[e][1] * 0.07}, ${lista[e][1] * 0.12}, ${lista[e][1] - (lista[e][1] * 0.07) - (lista[e][1] * 0.012)}"])
            print("\nSe ha añadido otra tabla a 'Reporte de sueldos.csv' para los datos sin truncar")
            input("Presione ENTER para continuar")

#----------------------------------------------------------------Interfaz salir del programa-------------------------------------------------------------------

def salirDePrograma():
    for a in range(4):
        os.system("cls")
        print("Saliendo del programa", "."*a, sep="")
        time.sleep(1)
    print("Desarrollado por Lucas Olmedo\n21.141.971-7")
    
#----------------------------------------------------------------Menu principal--------------------------------------------------------------
        
while opc != 6:
    try:
        os.system("cls")
        opc = int(input("Bienvenido al registro de datos de trabajadores\n>¿Que es lo que quiere hacer?\n[1] Mostrar tabla de trabajadores\n[2] Asignar sueldos aleatorios\n[3] Clasificar sueldos\n[4] Ver estadisticas de sueldo\n[5] Reportes de sueldo (.csv)\n[6] Salir del programa\n>"))
    except ValueError:
        print("Valor no reconocible")
        time.sleep(2)
    else:
        match opc:
            case 1:
                mostrarTabla(trabajadores)
            case 2:
                if asignacionDeSueldos == False:
                    asignacionDeSueldos = True
                    trabajadores = asignarSueldosAleatorios(trabajadores)
                else:
                    print("Los sueldos ya estan asignados")
                    time.sleep(2)
            case 3:
                if asignacionDeSueldos == False:
                    print("No puede acceder aqui si aun no ha asignado los sueldos")
                    time.sleep(2)
                else:
                    clasificarSueldos(trabajadores)
            case 4:
                if asignacionDeSueldos == False:
                    print("No puede acceder aqui si aun no ha asignado los sueldos")
                    time.sleep(2)
                else:
                    estadisticasDeSueldo(trabajadores)
            case 5:
                if asignacionDeSueldos == False:
                    print("No puede acceder aqui si aun no ha asignado los sueldos")
                    time.sleep(2)
                else:
                    reporteDeSueldos(trabajadores)
            case 6:
                salirDePrograma()
            case _:
                print("Opcion fuera de rango")
                time.sleep(2)