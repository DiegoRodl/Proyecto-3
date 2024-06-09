import textwrap
from random import randrange as aleatorio
from art import *

def instrucciones():
    while True:
        print("Instrucciones del Juego")
        print("1. Objetivo del Juego")
        print("2. Descripción del Tablero")
        print("3. Reglas del Juego")
        print("4. Consejos para Jugar")
        print("5. Volver al Menú Principal")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            mostrar_informacion("""
El objetivo principal del juego es simular la lucha de las comunidades recuperadoras
en su intento por mantener la sostenibilidad de su entorno. Los jugadores deben
gestionar recursos, mejorar sus comunidades y defenderse de ataques para asegurar
la supervivencia y el bienestar de su población.
            """,opcion)
            
        elif opcion == '2':
            mostrar_informacion("""
Descripción del Tablero:
El tablero representa el área de la comunidad, dividido en casillas que corresponden
a diferentes partes del territorio. Cada casilla puede contener recursos, infraestructuras
o elementos que los jugadores pueden utilizar para desarrollar su comunidad.
El diseño del tablero permite a los jugadores visualizar y planificar sus movimientos
estratégicos de manera efectiva.
            """,opcion)
            
        elif opcion == '3':
            opcion='z'
            mostrar_informacion("""
Reglas del Juego:
1. Cada jugador comienza con un conjunto de recursos básicos.
2. El tablero está dividido en casillas que representan diferentes áreas de la comunidad.
3. Los jugadores deben asignar tareas a sus habitantes para recolectar recursos,
mejorar infraestructuras y defender la comunidad.
4. Los turnos se alternan entre los jugadores, y cada turno consiste en un número
limitado de acciones.
5. Los ataques de otras comunidades o desastres naturales pueden ocurrir
aleatoriamente, y los jugadores deben estar preparados para responder.
            """,opcion)
            
        elif opcion == '4':
            opcion='z'
            mostrar_informacion("""
 Consejos para Jugar:
    - Prioriza la recolección de recursos esenciales al inicio del juego para asegurar
      la supervivencia.
    - Mejora las infraestructuras clave que aumentan la eficiencia de tu comunidad.
    - Distribuye a tus habitantes de manera equilibrada para mantener un crecimiento
      sostenible.
    - Mantente alerta a las señales de posibles ataques y fortalece tus defensas
      cuando sea necesario.
    - Colabora con otras comunidades cuando sea posible para enfrentar amenazas comunes.
            """,opcion)
            
            
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
        print("3. Información sobre SolarPunk")
        print("4. Información sobre Pueblos Originarios")
        print("5. Información sobre el conflicto en Cabagra, Costa Rica")
        print("6. Referencias")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            return jugar()
        
        elif opcion == '2':
            instrucciones()
            
        elif opcion == '3':
            mostrar_informacion("""
El solarpunk es un movimiento cultural y estético que imagina un futuro sostenible y ecológicamente armonioso. 
A diferencia de otros géneros de ciencia ficción, el solarpunk presenta un enfoque optimista sobre lo que podría ser el futuro 
si logramos resolver los problemas ambientales y sociales actuales. En este sentido, la tecnología juega un papel crucial, 
ya que se integra con la naturaleza para crear ciudades verdes y autosuficientes. Por ejemplo, en una nueva Detroit imaginada 
en la ficción solarpunk, el sistema tecnológico empleado se basa en la obtención de electricidad mediante paneles solares 
estratégicamente colocados para maximizar la energía solar, junto con la implementación de inteligencia artificial para hacer 
más eficiente la gestión energética (Withycombe Keeler, 2018). Sin embargo, esta utopía no está exenta de problemas; 
la imposición de un gobierno algorítmico mecanicista no siempre considera las particularidades individuales del ecosistema 
ni las consecuencias ecológicas de dicho sistema (Hudson, 2018). Además, el solarpunk se distingue por su enfoque sociopolítico 
y económico revolucionario, que reconoce la necesidad de combatir los problemas contemporáneos en múltiples frentes 
para crear un futuro positivo para todos los seres vivos (Kroon, 2019). A pesar de las críticas al enfoque tecnoutópico, 
las propuestas solarpunk combinan la cooperación entre organismos animales, vegetales y ecosistémicos, respaldadas por teorías actuales 
dentro de las humanidades ambientales y los estudios de la energía, ofreciendo una visión de esperanza y sostenibilidad.
            """,opcion)   
            
        elif opcion == '4':
            mostrar_informacion("""
Los pueblos originarios, a menudo sujetos a estereotipos y percepciones erróneas, son vistos a través de un prisma que los presenta
como homogéneos y estrechamente vinculados a prácticas y tradiciones rudimentarias. En muchos sistemas educativos, persisten ideas
preconcebidas que sugieren que las personas indígenas solo hablan lenguas vernáculas y que todos ellos tienen una relación innata con la
"madre tierra". Estas representaciones no solo son simplistas sino también incorrectas, ya que ignoran la diversidad y la riqueza cultural
de estos pueblos. Por ejemplo, las representaciones comunes incluyen la creencia de que las comunidades indígenas viven en condiciones
rudimentarias y mantienen una relación única y protectora con el medio ambiente. Sin embargo, la realidad es que muchos pueblos indígenas han
adoptado herramientas modernas y su vida cotidiana no es muy diferente a la del resto de la población costarricense; habitan en casas de cemento
y visten de manera similar. Las autorrepresentaciones de los pueblos originarios, por otro lado, muestran un orgullo por la pertenencia a su comunidad
y un fuerte compromiso con la preservación de sus características culturales y tradiciones. Las comunidades, como la de los malekus, han experimentado
cambios en su organización social debido a factores económicos, generacionales y ambientales, desafiando aún más los estereotipos prevalentes.
Este contexto subraya la necesidad de una comprensión más matizada y respetuosa de los pueblos originarios, reconociendo tanto su diversidad interna como
su capacidad para adaptarse y evolucionar en un mundo moderno.
            """,opcion)
            
        elif opcion == '5':
            mostrar_informacion("""
Los conflictos en los territorios indígenas de Costa Rica han escalado recientemente, extendiéndose de Salitre a Cabagra. Estos conflictos surgen
principalmente por disputas de tierras entre las comunidades indígenas y no indígenas. En Salitre, la comunidad indígena ha enfrentado invasiones
de tierras y violencia, mientras que en Cabagra, la tensión ha aumentado debido a la ocupación de tierras indígenas por parte de no indígenas.
Las autoridades locales y nacionales han intervenido para intentar resolver estas disputas, pero las medidas tomadas no han sido suficientes para
garantizar la seguridad y el respeto de los derechos territoriales indígenas. Las comunidades indígenas continúan luchando por la recuperación de
sus tierras ancestrales, enfrentándose a amenazas y violencia en el proceso. Esta situación resalta la necesidad de una mayor protección y reconocimiento
de los derechos territoriales de los pueblos indígenas, así como de un diálogo inclusivo y efectivo para resolver estos conflictos de manera pacífica y sostenible.
            """,opcion)
            
        elif opcion == '6':
            opcion='z'
            mostrar_informacion("""
1)De, C., Ciencia, L. A., Solarpunk, F., & Rivero-Vadillo, A.Estudios humanísticos. Filología. University of Leon. 10.18002/ehf

2)Naranjo Segura, J. C., & Bolaños-Alvarado, C. (2023). Los pueblos originarios de Costa Rica y la construcción de su imaginario desde la enseñanza de los Estudios Sociales: el caso maleku.
Universidad de Costa Rica. 10.15517/h.v13i2.52966

3)Delfino.cr. (2020, 10 de febrero). Conflictos en territorios indígenas salen de Salitre y llegan también a Cabagra. Delfino.cr. https://delfino.cr/2020/02/conflictos-en-territorios-indigenas-
salen-de-salitre-y-llegan-tambien-a-cabagra
             """,opcion)
                     
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intenta de nuevo.")
#-------------------------------------------------------
   
def mostrar_informacion(info,opcion):
    """
    funcion que mostrara el texto de manera correcta
    """
    if opcion == 'z':
        
        print("")
        print(info)
        print("")
        input("Presiona Enter para regresar al menú anterior...")
        
        
    else:
        
        info_colocada = textwrap.fill(info, width=85)
        print("")
        print(info_colocada)
        print("")
        input("Presiona Enter para regresar al menú anterior...")
#-------------------------------------------------------
    
def numero_entero(cadena):
    """funcion que revisa si un numero es entero o es una letra o un simbolo
    E: texto del mensaje
    S: true o false
    """
    if cadena == "":
        return True
    else:
        primer_digito = cadena[0]
        
        if primer_digito == "0" or \
        primer_digito == "1" or \
        primer_digito == "2" or \
        primer_digito == "3" or \
        primer_digito == "4" or \
        primer_digito == "5" or \
        primer_digito == "6" or \
        primer_digito == "7" or \
        primer_digito == "8" or \
        primer_digito == "9"or \
        primer_digito == "10001":
            return numero_entero(cadena[1:])
        
        else:
            return False

#-------------------------------------------------------
def obtener_entero(mensaje):
    """
    funcion que valida si el dato puede llegar a ser un entero o no
    E: mensaje
    S: valor que pidio cambiado a int
    """
    valor = input(mensaje)
    if valor =="" or valor == " ":
        print ("Error, debes de eligir algun número no letras ni simbolos")
        return obtener_entero(mensaje)
    elif numero_entero(valor)==False:
        print ("Error, debes de eligir algun número no letras ni simbolos")
        return obtener_entero(mensaje)
    
    else:
        return int(valor)
#-------------------------------------------------------    
def solicitar_dimensiones():
    """
    funcion que inicia el juego y pedira los datos para crear las filas y columnas del tablero
    """

    filas=obtener_entero("Ingrese el numero de filas a colocar en el tablero, el minimo es 3 y maximo 9: ")
    columnas=obtener_entero("Ingrese el numero de columnas a colocar en el tablero, minimo es 3 y maximo 9: ")


    if 3 <= filas <= 9 and 3 <= columnas <= 9:
        return filas, columnas

    
    else:
        print("Por favor, ingrese valores dentro del rango permitido (3-9).")
        return solicitar_dimensiones()
    
#------------------------------------------------------- 
def crear_matriz(filas, columnas):
    return [["⬜"for _ in range(columnas)] for _ in range(filas)]

#------------------------------------------------------- 
def crear_matriz(filas, columnas):
    """
    Función que crea la matriz
    E: Las dilas y columnas elegidas por el jugador
    S: La matriz
    R: Solo acepta esas filas y columnas
    """
    return [["_"for _ in range(columnas)] for _ in range(filas)]

#------------------------------------------------------- 
def jugar():
    """
    Función que hace la matriz
    E: Nada
    S: La matriz printeada
    R: Nada
    """
    print(text2art("Bienvenido jugador"))
    filas, columnas = solicitar_dimensiones()
    matriz = crear_matriz(filas, columnas)
    return mostrar_matriz(matriz)

#------------------------------------------------------- 
def mostrar_matriz(matriz):
    """
    Función que printea la matriz
    E: La matriz de juego
    S: La matriz printeada
    R: Solo acepta esa matriz
    """
    for fila in matriz:
        print(fila)
    return inicio_juego(matriz)

#-------------------------------------------------------
def mostrar_matriz_juego(matriz):
    """
    Función que printea la matriz
    E: La matriz de juego
    S: La matriz printeada
    R: Solo acepta esa matriz
    """
    for fila in matriz:
        print(fila)
    return " "

#------------------------------------------------------- 
def turno_jugador(matriz):

    """
    Función que hace los turnos de los jugadores
    E:Nada
    S: El turno del jugador
    R: Ninguna
    """
    print(" ")
    turno = input("Escoja entre P (Proyecto), I (Iniciativa) o C (Cultura): ")
    print(f"Ha escogido {turno}")
    print(" ")
    posición_fi = input(f"Escoja la fila que desea debe ser entre 0 y {len(matriz) - 1}: ")
    posición_co = input(f"Escoja la columna que desea debe ser entre 0 y {len(matriz[0]) - 1}: ")
    print(f"Ha escogido la la posición {posición_fi}, {posición_co}")

    if revisar_turno(turno) != True:
        print(" ")
        print("Error, debe ser una de las opciones mencionadas, intente de nuevo")
        return turno_jugador(matriz)
    
    elif revisar_fila(matriz, posición_fi) != True or revisar_columna(matriz, posición_co) != True:
        print(" ")
        print("Error, debe ingresar un número o un valor válido para la posición, intente de nuevo")
        return turno_jugador(matriz)

    else:
        return juego(matriz, turno, int(posición_fi), int(posición_co))

#------------------------------------------------------- 
def revisar_turno(turno):
    """
    Función que revisa si el turno es válido
    E: El turno del jugador
    S: True si es válido o false en caso de que no
    R: Solo acepta el turno
    """
    if type(turno) != str:
        return False
    
    elif turno.upper() == "P" or turno.upper() == "I" or turno.upper() == "C":
        return True
    
    else:
        return False

#------------------------------------------------------- 
def revisar_fila(matriz, fila):
    """
    Función que revisa si la fila es permitida
    E: La fila del jugador y la matriz de juego
    S: True si está permitida, False en caso de que no
    R:Solo acepta la fila ingresada por el jugador
    """

    if numero_entero(fila) != True:
        return False
    
    elif fila == " " or fila == "":
        return False
    
    else:
        fila = int(fila)
        if fila < 0 or fila >= len(matriz):
            return False
        
        else:
            return True
        
#------------------------------------------------------- 
def revisar_columna(matriz, columna):
    """
    Función que revisa si la fila es permitida
    E: La fila del jugador y la matriz de juego
    S: True si está permitida, False en caso de que no
    R:Solo acepta la fila ingresada por el jugador
    """

    if numero_entero(columna) != True:
        return False
    
    elif columna == " " or columna == "":
        return False
    
    else:
        columna = int(columna)
        if columna < 0 or columna >= len(matriz[0]):
            return False
        
        else:
            return True
        
#------------------------------------------------------- 
def juego(matriz, turno, fila, columna):
    """
    Función que lleva acabo las acciones de la opción escogida por el juagdor
    E:Las opciones escogidas por el jugador y la matriz  
    S: La matriz con los cambios necesarios
    R: Solo acepta lo antes mencionado
    """
    if type(turno) != str:
        return "Error"

    elif turno.upper() == "P":
        matriz[fila][columna] = turno.upper()
        return iniciativa(matriz, fila, columna)
    
    elif turno.upper() == "C":
        matriz[fila][columna] = turno.upper()
        return cultura(matriz, fila, columna)
    
    elif turno.upper() == "I":
        matriz[fila][columna] = turno.upper()
        return iniciativa(matriz, fila, columna)
    
    else:
        return 

#------------------------------------------------------- 
def proyecto(matriz):
    """
    Función que revisa si el juego debe acabar, ver quién gana o no
    E: La matriz de juego
    S: Un mensaje de ganador o la matriz, seún qué pase
    R: Solo acepta la matriz de juego
    """
    contador_1 = 0
    contador_2 = 0
    

    while contador_2 < len(matriz[0]):

        if matriz[0][contador_2] == "P":

            contar = 1
            while True:
                

                if matriz[contar][contador_2] == "P":
                    contar += 1
                    
                    if contar == len(matriz):
                        return ganar()
                    
                    else: 
                        continue
            
                else: 
                    
                    break
            contador_2 += 1
        else: 
            contador_2 += 1
    
    while contador_1 < len(matriz):

        if matriz[contador_1][0] == "P":

            contar = 1
            while True:
                

                if matriz[contador_1][contar] == "P":
                    contar += 1
                    
                    if contar == len(matriz[0]):
                        return ganar()
                    
                    else: 
                        continue
            
                else: 
                    
                    break
            contador_1 += 1
        else: 
            contador_1 += 1
    
    return matriz

#------------------------------------------------------- 
def cultura(matriz, fila, columna):
    """
    Función que despliega las culturas
    E: La matriz y la fila y columna que ingresó el jugador
    S: La matriz de juego
    R: Solo acepta lo antes dicho
    """
    contador_1 = 0
    contador_2 = 0

    while contador_2 < len(matriz[0]):

        if matriz[fila][contador_2] == "P":
            break

        else: 
            matriz[fila][contador_2] = "C"
            contador_2 += 1

    contador_2 = 0

    while contador_2 > 0:
        if matriz[fila][contador_2] == "P":
            break

        else: 
            matriz[fila][contador_2] = "C"
            contador_2 -= 1
    
    while contador_1 < len(matriz):
        if matriz[contador_1][columna] == "P":
            break

        else:
            matriz[contador_1][columna] = "C"
            contador_1 += 1
    
    contador_1 = 0
    
    while contador_1 > 0:
        if matriz[contador_1][columna] == "P":
            break

        else:
            matriz[contador_1][columna] = "C"
            contador_1 -= 1



    return iniciativa(matriz, fila, columna)

#------------------------------------------------------- 
def iniciativa(matriz, fila, columna):
    """
    Función que revisa si hay iniciativas para convertir en proyectos
    E: La matriz de juego
    S: Un mensaje de ganador o la matriz, según qué pase
    R: Solo acepta la matriz de juego
    """
    contador_1 = 0
    contador_2 = 0
    
    for i in matriz:

        for caracter in i:

            if contador_1 == fila and contador_2 == columna:
                contador_2 += 1
                continue

            else:

                if caracter == "I":
                    matriz[contador_1][contador_2] = "P"
                    contador_2 += 1
                    continue
                else:
                    contador_2 += 1
                    continue
        contador_2 = 0
        contador_1 += 1

    
    return proyecto(matriz)

#-------------------------------------------------------
def ganar():
    """
    Función con el mensaje de ganar
    """
    return "Has ganado, felicidades"

#-------------------------------------------------------
def turno_máquina(matriz):
    """
    Función que hace el turno de la noche o la máquina
    E: La matriz de juego
    S: La matriz de la máquina o si el jugador perdió
    R: Solo acepta la matriz de juego
    """
    numero = aleatorio(0, len(matriz))
    print(" ")
    print(f"Los terrenos usurpado serán {numero}")
    print(" ")


    while numero > 0:
        number_1 = aleatorio(0, len(matriz))
        number_2 = aleatorio(0, len(matriz[0]))


        if matriz[number_1][number_2] == "P":
            matriz[number_1][number_2] = "U"
            numero -= 1
        
        elif matriz[number_1][number_2] == "I":
            numero -= 1
            continue

        elif matriz[number_1][number_2] == "C":
            matriz[number_1][number_2] = "_"
            numero -= 1
        
        else:
            matriz[number_1][number_2] = "U"
            numero -= 1

    return máquina(matriz)

#-------------------------------------------------------
def máquina(matriz):
    """
    Función que revisa si la máquina ha ganado
    E: La matriz de juego
    S: La matriz de juego o el mensaje de perder
    R: Solo acepta la matriz
    """
    contador_1 = 0
    contador_2 = 0

    

    while contador_2 < len(matriz[0]):

        if matriz[0][contador_2] == "U":

            contar = 1
            while True:
                

                if matriz[contar][contador_2] == "U":
                    contar += 1
                    
                    if contar == len(matriz):
                        return perdido()
                    
                    else: 
                        continue
            
                else: 
                    
                    break
            contador_2 += 1
        else: 
            contador_2 += 1
    
    while contador_1 < len(matriz):

        if matriz[contador_1][0] == "P":

            contar = 1
            while True:
                

                if matriz[contador_1][contar] == "U":
                    contar += 1
                    
                    if contar == len(matriz[0]):
                        return perdido()
                    
                    else: 
                        continue
            
                else: 
                    
                    break
            contador_1 += 1
        else: 
            contador_1 += 1
    
    return matriz
#-------------------------------------------------------
def perdido():
    """
    Función con el mensaje de perder
    """
    return "Has perdido, inténtalo de nuevo"

#------------------------------------------------------- 
def inicio_juego(matriz):
    """
    Función que inicia y lleva el juego acabo
    E: La matriz de juego
    S: El juego como tal
    R: Solo acepta esa matriz
    """
    matriz_dia = turno_jugador(matriz)

    if matriz_dia == "Has ganado, felicidades":
        print(" ")
        print(text2art("El juego ha terminado"))
        print(text2art("Has ganado"))
        return print(text2art("Felicidades"))

    print(" ")
    mostrar_matriz_juego(matriz_dia)
    
    matriz_noche = turno_máquina(matriz_dia)
    
    if matriz_noche == "Has perdido, inténtalo de nuevo":
        print(" ")
        print(text2art("El juego ha terminado"))
        print(text2art("Has perdido"))
        return print(text2art("Intentalo de nuevo"))
    print(" ")
    mostrar_matriz_juego(matriz_noche)

    
    return inicio_juego(matriz_noche)
menu_principal()
