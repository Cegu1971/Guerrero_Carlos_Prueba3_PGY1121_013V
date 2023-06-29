import os
import time
import numpy as np
def auto():
    a1 = True
    a2 = True
    a3 = True
    a4 = True
    a5 = True
    a6 = True
    a7 = True
    a8 = True
    tipo = ""
    patente = ""
    marca = ""
    opc = 0
    multa = 0
    mfecha = ""
    vfecha = ""
    dueño = ""
    while a1:
        while a2:
            os.system('cls')
            patente = str(input("Ingrese la patente del vehículo:\n"))
            if len(patente) == 6:
                a2 = False
            else:
                print("Patente erronea")
                time.sleep(1)
        while a3:
            os.system('cls')
            tipo = str(input("Ingrese el modelo del vehiculo:\n"))
            if tipo == "":
                print("Debe ingresar datos")
                time.sleep(1)
            else:
                a3 = False
        while a4:
            os.system('cls')
            marca = str(input("Ingrese el marca del vehiculo:\n"))
            if len(marca) >= 2 and len(marca) <= 15:
                a4 = False
            else:
                print("Modelo no aceptado")
                time.sleep(1)
        while a5:
            os.system('cls')
            precio = int(input("Ingrese el precio del vehiculo:\n"))
            if precio > 5000000:
                a5 = False
            else:
                print("Valor sobre los $ 5.000.000")
                time.sleep(1)
        while a6:
            os.system('cls')
            print("El vehiculo tiene multa   1. SI  2. NO")
            opc = int(input("\nQue opcion desea eliger\n"))
            if opc > 0 and opc < 3:
                if opc == 2:
                    multa = 0
                    mfecha = "sin fecha"
                    a6 = False
                else:
                    multa = int(input("Ingrese el valor de la multa:\n"))
                    mfecha = str(input("Ingrese la fecha de la multa:\n"))
                    a6 = False
            else:
                print("Opción erronea")
                time.sleep(1)
        while a7:
            os.system('cls')
            vfecha = str(input("Ingrese la fecha del registro del vehículo:\n"))
            if len(vfecha) >= 8:
                a7 = False
            else:
                print("Fecha muy corta, largo minimo 8")
                time.sleep(1)
        while a8:
            os.system('cls')
            dueño = str(input("Ingrese nombre del dueño del vehiculo:\n"))
            a8 = False
            ingresos = [patente, tipo, marca, precio, multa, mfecha, vfecha, dueño]
            print(ingresos)
            time.sleep(2)
        return(ingresos)
    a1 = False

def buscar():
    os.system('cls')
    print("Opción en mantención")
    print("No me quiso salir la lista. Pido mis puntos pendientes")
    time.sleep(2)
    
def imprimir():
    os.system('cls')
    print("Opción en mantención")
    print("No me quiso salir la lista. Pido mis puntos pendientes")
    time.sleep(2)

