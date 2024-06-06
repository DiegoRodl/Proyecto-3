def instrucciones():
    while True:
        print("Instrucciones del Juego")
        print("1. Objetivo del Juego")
        print("2. Controles")
        print("3. Reglas del Juego")
        print("4. Estrategias")
        print("5. Volver al Menú Principal")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            mostrar_informacion("Aquí va el objetivo del juego...")
        elif opcion == '2':
            mostrar_informacion("Aquí van los controles del juego...")
        elif opcion == '3':
            mostrar_informacion("Aquí van las reglas del juego...")
        elif opcion == '4':
            mostrar_informacion("Aquí van las estrategias del juego...")
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
#------------------------------------------------------------------------ 
def menu_principal():
    while True:
        print("Menú Principal")
        print("1. Jugar")
        print("2. Instrucciones del Juego")
        print("3. Información de Costa Rica")
        print("4. Información los indígenas")
        print("5. Referencias")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            return jugar()
        elif opcion == '2':
            instrucciones()
        elif opcion == '3':
            mostrar_informacion("Aquí va la información de Costa Rica...")
        elif opcion == '4':
            mostrar_informacion("Aquí va la información sobre los indígenas...")
        elif opcion == '5':
            mostrar_informacion("Aquí van las referencias...")
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
#------------------------------------------------------------------------            
def jugar():
    print("Iniciando el juego...")


    
def mostrar_informacion(info):
    print(info)
    input("Presiona Enter para regresar al menú anterior...")


menu_principal()
