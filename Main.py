from Funciones import auto,buscar,imprimir
import time
import os
import numpy as np
menu = True
datos = []
while menu:
    os.system("cls")
    print("***    MENU  AUTO SEGURO    ***")
    print("")
    print("1. Ingreso de Datos del Vehículo")
    print("2. Buscar información del Vehículo")
    print("3. Imprimir Certificados")
    print("4. Salir")
    print(" ")
    try:
        entrada = int(input("\nQue opcion desea eliger\n"))
        if (entrada > 0 and entrada < 5):
            if (entrada == 1):
                auto()
                datos.append(auto())
                print(datos)
            elif (entrada == 2):
                buscar()
            elif (entrada == 3):
                imprimir()
            elif (entrada == 4):
                menu = False
        else:
            print("no existe esa opcion")
            time.sleep(2)
    except:
        print("opcion invalida")
        time.sleep(2)
print("\nGracias por visitar AUTO SEGURO")
print("Carlos Guerrero U. - Versión 1.2")
print(" ")
time.sleep(2)   