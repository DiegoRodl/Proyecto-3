import textwrap

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
    if opcion == '6':
        
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
def jugar():
    filas, columnas = solicitar_dimensiones()
    matriz = crear_matriz(filas, columnas)
    for fila in matriz:
        print(fila)
    return matriz 

menu_principal()
