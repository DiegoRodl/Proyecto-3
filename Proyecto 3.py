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
        print("5. Información sobre el conflicto en Cabaga, Costa Rica")
        print("6. Referencias")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            return jugar()
        
        elif opcion == '2':
            mostrar_informacion("""""")
            
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
            """)   
            
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
            """)
            
        elif opcion == '5':
            mostrar_informacion("Aquí van la Información sobre el conflicto en Cabaga")
            
        elif opcion == '6':
            mostrar_informacion("Aquí van las referencias...")
            
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intenta de nuevo.")
#------------------------------------------------------------------------            
def jugar():
    print("Iniciando el juego...")


    
def mostrar_informacion(info):
    """
    funcion que mostrara el texto de manera correcta
    """
    info_colocada = textwrap.fill(info, width=85)
    print("")
    print(info_colocada)
    print("")
    input("Presiona Enter para regresar al menú anterior...")

menu_principal()
